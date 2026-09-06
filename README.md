# Product Funnel Analysis
Simple product funnel analysis using Python and pandas.

## About the project
I analyzed a small synthetic dataset of user events to understand how users move through a product funnel.

The funnel consists of four stages:

Registration → Product View → Add to Cart → Purchase

## Results
| Stage | Users | Conversion |
|------|------:|-----------:|
| Registration | 15 | 100% |
| Product View | 14 | 93.3% |
| Add to Cart | 10 | 66.7% |
| Purchase | 6 | 40.0% |

## Key findings
- 15 users registered.
- 6 users completed a purchase.
- Overall conversion from registration to purchase was 40%.
- The largest drop-off occurred between Product View and Add to Cart.

## Tools
- Python
- pandas
- matplotlib

## Files
- `events.csv` — user events
- `analysis.py` — funnel analysis
- `product_funnel.png` — visualization
