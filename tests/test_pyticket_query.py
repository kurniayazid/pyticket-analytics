from pyticket_analytics import pyticket_query
from dotenv import load_dotenv
import pandas as pd
import os
load_dotenv()

key = os.getenv('YOUR_CONSUMER_KEY')
secret = os.getenv('YOUR_CONSUMER_SECRET')

# Importing pytest
import pytest

## Testing single letter word
def test_pyticket_query():
    dataframe = type(pyticket_query('brooklyn nets',apikey=key))
    expected = type(pd.DataFrame)
    assert dataframe == expected