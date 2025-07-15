import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextProcessor:
    def __init__(self, api_key=None):
        """
        Initialize TextProcessor with API key
        :param api_key: API key for Google's Generative AI
        """
        load_dotenv()
        if api_key is None:
            api_key = os.getenv('GOOGLE_API_KEY')
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    async def analyze_text(self, text: str):
        """Analyze product description text and return structured data"""
        try:
            analysis_prompt = f"""Analyze this product description and provide detailed information in the following format exactly:

BEGIN_ANALYSIS
Product Name: [extract product name]
Category: [main category/subcategory]
Key Features:
- [feature 1]
- [feature 2]
- [feature 3]
Target Audience: [intended users]
Price Range: [if mentioned]
USP: [unique selling proposition]
Keywords:
- [keyword 1]
- [keyword 2]
- [keyword 3]
END_ANALYSIS

Text to analyze: {text}"""
            
            response = self.model.generate_content(analysis_prompt)
            analysis_dict = self._parse_analysis(response.text)
            analysis_dict['status'] = 'success'
            
            return analysis_dict
            
        except Exception as e:
            logger.error(f"Error in analyze_text: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def _parse_analysis(self, text):
        """Parse the analysis text into structured format"""
        analysis_dict = {
            'product_name': '',
            'category': '',
            'key_features': [],
            'target_audience': '',
            'price_range': '',
            'usp': '',
            'keywords': []
        }
        
        try:
            if 'BEGIN_ANALYSIS' in text and 'END_ANALYSIS' in text:
                content = text.split('BEGIN_ANALYSIS')[-1].split('END_ANALYSIS')[0].strip()
            else:
                content = text.strip()
            
            lines = content.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                if line.startswith('Product Name:'):
                    analysis_dict['product_name'] = line.split(':', 1)[1].strip()
                elif line.startswith('Category:'):
                    analysis_dict['category'] = line.split(':', 1)[1].strip()
                elif line.startswith('Target Audience:'):
                    analysis_dict['target_audience'] = line.split(':', 1)[1].strip()
                elif line.startswith('Price Range:'):
                    analysis_dict['price_range'] = line.split(':', 1)[1].strip()
                elif line.startswith('USP:'):
                    analysis_dict['usp'] = line.split(':', 1)[1].strip()
                elif line.startswith('Key Features:'):
                    current_section = 'features'
                elif line.startswith('Keywords:'):
                    current_section = 'keywords'
                elif line.startswith('- '):
                    if current_section == 'features':
                        analysis_dict['key_features'].append(line.strip('- '))
                    elif current_section == 'keywords':
                        analysis_dict['keywords'].append(line.strip('- '))
            
            return analysis_dict
            
        except Exception as e:
            logger.error(f"Error parsing analysis: {str(e)}")
            return analysis_dict
