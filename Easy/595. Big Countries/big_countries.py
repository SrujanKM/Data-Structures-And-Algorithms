# LeetCode Problem 595: Big Countries
# Link: https://leetcode.com/problems/big-countries/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    Filters out countries that are considered 'big' based on:
    - area >= 3,000,000 OR
    - population >= 25,000,000

    Returns a DataFrame with only the 'name', 'population', and 'area' columns.
    """
    # Apply the filtering condition
    big = world[
        (world["area"] >= 3_000_000) |
        (world["population"] >= 25_000_000)
    ]
    
    # Select the required columns
    return big[["name", "population", "area"]]


if __name__ == "__main__":
    # ✅ Sample test input
    data = {
        "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
        "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
        "area": [652230, 28748, 2381741, 468, 1246700],
        "population": [25500100, 2831741, 37100000, 78115, 20609294],
        "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
    }

    # ✅ Convert to DataFrame
    df = pd.DataFrame(data)

    # ✅ Call the function and print the result
    result = big_countries(df)
    print(result)
