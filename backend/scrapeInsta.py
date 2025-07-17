import httpx
import json
from typing import Dict
from urllib.parse import quote
import jmespath

INSTAGRAM_DOCUMENT_ID = "8845758582119845"  # constant id for post documents

def scrape_post(url_or_shortcode: str) -> Dict:
    """Scrape single Instagram post or reel data"""
    # Determine if the URL is a Reel or a Post
    if "http" in url_or_shortcode:
        if "/reel/" in url_or_shortcode:
            shortcode = url_or_shortcode.split("/reel/")[-1].split("/")[0]  # Handle Instagram Reels
        elif "/p/" in url_or_shortcode:
            shortcode = url_or_shortcode.split("/p/")[-1].split("/")[0]  # Handle regular posts
        else:
            print("Unknown URL format.")
            return {}
    else:
        shortcode = url_or_shortcode

    print(f"Scraping Instagram post/reel: {shortcode}")

    variables = quote(json.dumps({
        'shortcode': shortcode,
        'fetch_tagged_user_count': None,
        'hoisted_comment_id': None,
        'hoisted_reply_id': None
    }, separators=(',', ':')))

    body = f"variables={variables}&doc_id={INSTAGRAM_DOCUMENT_ID}"
    url = "https://www.instagram.com/graphql/query"

    try:
        result = httpx.post(
            url=url,
            headers={"content-type": "application/x-www-form-urlencoded"},
            data=body
        )
        result.raise_for_status()  # Raise an exception for HTTP errors
        data = result.json()  # Parse JSON response directly
        return data.get("data", {}).get("xdt_shortcode_media", {})
    except httpx.RequestError as e:
        print(f"Request error: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return {}

def parse_post(data: Dict) -> Dict:
    """Parse relevant fields from Instagram post or reel data"""
    result = jmespath.search("""{
        src: display_url,
        src_attached: edge_sidecar_to_children.edges[].node.display_url,
        video_url: video_url,
        type: product_type,
        video_duration: video_duration,
        captions: edge_media_to_caption.edges[].node.text,
        comments: edge_media_to_parent_comment.edges[].node.{
            id: id,
            text: text,
            created_at: created_at,
            owner: owner.username,
            owner_verified: owner.is_verified,
            viewer_has_liked: viewer_has_liked,
            likes: edge_liked_by.count
        }
    }""", data)
    return result

def save_to_json(data: Dict, filename: str):
    """Save the parsed data to a JSON file, overwriting the file if it exists."""
    try:
        # Save the new data, overwriting the existing file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([data], f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")


# Example usage:
url = "https://www.instagram.com/p/DBbc-7YvXYl/"  # Replace with the actual Instagram post URL
post_data = scrape_post(url)

# If post data is successfully retrieved, parse it
if post_data:
    parsed_post = parse_post(post_data)
    # print(json.dumps(parsed_post, indent=2, ensure_ascii=False))
    save_to_json(parsed_post, "parsed_post_r.json")
    print("Save the product listing data to a JSON file.")
    # # Create product listing from the parsed post data
    # product_listing = create_product_listing(parsed_post)
    # # print(json.dumps(product_listing, indent=2, ensure_ascii=False))

    # # Save the product listing data to a JSON file (appending)
    # save_to_json(product_listing, "product_listing.json")
else:
    print("Failed to retrieve post data.")



import heapq
n, nmr, ct = map(int, input().split())
minheap = []
for i in range(n):
    minheap.append(list(map(int, input().split())))
    minheap[-1].append(i)

heapq.heapify(minheap)
li = -1
lfi = -1
rfi = -1
i = 0
s = 0
while(i<nmr): 
    fi, ri, index = heapq.heappop(minheap)
    if(li!=-1 and index != li):
        if(lfi+rfi<fi+ct):
            lfi = lfi + rfi
            s = s+ lfi+rfi
            heapq.heappush(minheap, [fi, ri, index])
        else:
            s = s + fi + ct
            lfi = fi
            rfi = ri
            li = index
            heapq.heappush(minheap, [fi+ri, ri, index])
    else:
        li = index
        lfi = fi
        rfi = ri
        s = s + fi
        heapq.heappush(minheap, [fi+ri, ri, index])
    i+=1
print(s)
    




