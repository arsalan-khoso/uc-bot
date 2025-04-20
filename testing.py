#!/usr/bin/env python3
# Example usage of PGW Auto Glass scraper

import logging
from Scrapers import new as PGWScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pgw_scraper.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    # Initialize the scraper
    scraper = PGWScraper()
    
    # Login with credentials
    # Note: Replace these with your actual credentials
    login_result = scraper.login(
        username="your_username", 
        password="your_password"
    )
    
    if not login_result["success"]:
        logger.error(f"Login failed: {login_result['message']}")
        return
    
    logger.info(f"Login successful in {login_result['time_taken']:.2f} seconds")
    
    # Search for parts
    # Replace with actual part numbers you need to search for
    part_numbers = [
        "FW01234", 
        "DW56789"
    ]
    
    for part_number in part_numbers:
        logger.info(f"Searching for part: {part_number}")
        
        search_result = scraper.search(part_number)
        
        if not search_result["success"]:
            logger.error(f"Search failed: {search_result['message']}")
            continue
        
        logger.info(f"Search completed in {search_result['time_taken']:.2f} seconds")
        
        # Process results
        if not search_result["results"]:
            logger.info(f"No results found for {part_number}")
            continue
        
        logger.info(f"Found {len(search_result['results'])} results for {part_number}")
        
        # Display results
        print(f"\nResults for part number {part_number}:")
        print("-" * 50)
        
        for i, result in enumerate(search_result["results"], 1):
            print(f"Result {i}:")
            print(f"  Part Number: {result['part_number']}")
            print(f"  Availability: {result['availability']}")
            print(f"  Price: {result['price']}")
            print(f"  Location: {result['location']}")
            print(f"  Supplier: {result['supplier']}")
            print("-" * 30)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Unexpected error: {str(e)}")