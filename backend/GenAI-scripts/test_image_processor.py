
import asyncio
import os
from image_processor import ImageProcessor
from text_processor import TextProcessor
import logging
import json
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'test_logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProcessorTester:
    def __init__(self, api_key=None):
        """
        Initialize ProcessorTester with optional API key
        :param api_key: API key for TextProcessor
        """
        if api_key is None:
            api_key = os.getenv('GOOGLE_API_KEY')
            if not api_key:
                raise ValueError("API key must be provided either through constructor or GOOGLE_API_KEY environment variable")
        
        self.image_processor = ImageProcessor()
        self.text_processor = TextProcessor(api_key=api_key)
        
    async def test_image_processor(self, image_paths):
        """Test the image processor with multiple images"""
        logger.info("Starting Image Processor Tests")
        
        results = []
        for image_path in image_paths:
            try:
                logger.info(f"Testing image: {image_path}")
                
                if not os.path.exists(image_path):
                    logger.error(f"Image file not found: {image_path}")
                    continue
                
                result = await self.image_processor.analyze_product(image_path)
                
                # Validate result structure
                expected_keys = [
                    'status', 'product_name', 'description', 
                    'key_features', 'specifications', 
                    'category', 'search_keywords'
                ]
                
                missing_keys = [key for key in expected_keys if key not in result]
                if missing_keys:
                    logger.warning(f"Missing keys in result: {missing_keys}")
                
                results.append({
                    'image_path': image_path,
                    'analysis': result,
                    'success': result.get('status') == 'success'
                })
                
                # Save individual result
                self._save_result(f"image_analysis_{os.path.basename(image_path)}.json", result)
                
            except Exception as e:
                logger.error(f"Error processing image {image_path}: {str(e)}")
                results.append({
                    'image_path': image_path,
                    'error': str(e),
                    'success': False
                })
        
        return results
    
    async def test_text_processor(self, test_texts):
        """Test the text processor with multiple text samples"""
        logger.info("Starting Text Processor Tests")
        
        results = []
        for i, text in enumerate(test_texts):
            try:
                logger.info(f"Testing text sample {i+1}")
                
                result = await self.text_processor.analyze_text(text)
                
                results.append({
                    'text_sample': text[:100] + '...' if len(text) > 100 else text,
                    'analysis': result,
                    'success': result.get('status') == 'success'
                })
                
                # Save individual result
                self._save_result(f"text_analysis_{i+1}.json", result)
                
            except Exception as e:
                logger.error(f"Error processing text sample {i+1}: {str(e)}")
                results.append({
                    'text_sample': text[:100] + '...',
                    'error': str(e),
                    'success': False
                })
        
        return results
    
    def _save_result(self, filename, data):
        """Save test results to file"""
        os.makedirs('test_results', exist_ok=True)
        filepath = os.path.join('test_results', filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved result to {filepath}")

async def main():
    # Set up API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        api_key = "AIzaSyCqeQCDhqqSbhz1tcKJrvr-ixtQa3TxTKY"  # Replace with your actual API key
    
    # Create test directory
    os.makedirs('test_images', exist_ok=True)
    
    # Test images
    test_images = [
        "A:/Users/VARSHA/Downloads/watch.jpg",
        "A:/Users/VARSHA/Downloads/sweaters.jpg",
        "A:/Users/VARSHA/Downloads/shoes.jpg"
    ]
    
    # Test texts
    test_texts = [
        """Premium Wireless Headphones: Experience superior sound quality with our latest noise-cancelling 
        headphones. Features include 30-hour battery life, premium leather cushions, and Bluetooth 5.0.""",
        
        """Smart Home Security Camera: 1080p HD video, night vision, two-way audio, and motion detection. 
        Works with Alexa and Google Home. Easy setup and free cloud storage.""",
        
        """Organic Green Tea Set: Premium Japanese green tea collection including Sencha, Gyokuro, and Matcha. 
        Each tea is carefully selected and packaged in traditional style containers."""
    ]
    
    try:
        tester = ProcessorTester(api_key=api_key)
        
        # Run tests
        logger.info("Starting processor tests...")
        
        # Test image processor
        image_results = await tester.test_image_processor(test_images)
        
        # Test text processor
        text_results = await tester.test_text_processor(test_texts)
        
        # Print summary
        logger.info("\nTest Summary:")
        logger.info(f"Images processed: {len(image_results)}")
        logger.info(f"Successful image analyses: {sum(1 for r in image_results if r.get('success'))}")
        logger.info(f"Texts processed: {len(text_results)}")
        logger.info(f"Successful text analyses: {sum(1 for r in text_results if r.get('success'))}")
        
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())






















