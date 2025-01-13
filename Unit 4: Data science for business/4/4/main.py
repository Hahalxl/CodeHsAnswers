import pandas as pd

google = pd.read_csv (r"google_books.csv")
goodreads = pd.read_csv (r"goodreads.csv")
pd.set_option("display.max_columns", None)
google.drop_duplicates(inplace=True)
goodreads.drop_duplicates(inplace=True)

# Compare columns from both datasets
# How many entries are in each dataset?
# How many columns are in each dataset?
print("Google Dataset")
print("-------------------")
print(google.info())
print()
print()
print("Goodreads Dataset")
print("-------------------")
print(goodreads.info())

# Goodreads Dataset - drop the extra columns

goodreads.drop(["bookID", "isbn", "isbn13", "language_code", "text_reviews_count"], axis=1, inplace=True)

# Goodreads Dataset - rename columns to match the google dataset

goodreads.rename(columns={"authors": "author", "average_rating": "rating", "num_pages": "page_count", "ratings_count": "voters", "publication_date": "published_date"}, inplace=True)

# Again - compare columns from both datasets
# Google has one extra column. What do you think might happen when we concatenate these?
# Do you think the order of the columns will matter?
print()
print()
print("Google Dataset")
print("-------------------")
print(google.info())
print()
print()
print("Goodreads Dataset")
print("-------------------")
print(goodreads.info())

# Concatenate the two datasets (add on as new rows)
google_and_goodreads = pd.concat([google, goodreads]).reset_index()
print()
print()
print("Google and Goodreads Dataset")
print("-------------------")
print(google_and_goodreads)

# Check the information from the new concatenated dataset.
# How many entries are there?
# What happened with the price column for the goodreads data?
print()
print()
print("Google and Goodreads Dataset")
print("-------------------")
print(google_and_goodreads.info())
