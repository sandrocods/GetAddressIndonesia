
# GetAddressIndonesia

Indonesia Postal Code, Village, Sub-district, District/regency. scraped from [Pos Indonesia](https://www.posindonesia.co.id/en)
save in sqlite database.



## Build With

 - [Python3](python.org)
 - [Requests](https://pypi.org/project/requests/)
 - [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
 - [Colorama](https://pypi.org/project/colorama/)


## Columns contains

| Column             | Type                                                                |
| ----------------- | ------------------------------------------------------------------ |
| id | Integer |
| desa | String |
| kecamatan | String |
| kabupaten_kota | String |
| kode_pos | String |



✅ Scraped at : 04/09/2022\
✅ Total : 9574 data\
✅ Database File : [data.db](https://github.com/sandrocods/GetAddressIndonesia/blob/master/data.db)

###

✅ Helpers Data : [data_list.json](https://github.com/sandrocods/GetAddressIndonesia/blob/master/data_list.json)\
✅ Contains : Data province, city, countyarea\
✅ 7336 Data Province and city unclean\
✅ 515 Data Clean
## Installation

Git clone [this project](https://github.com/sandrocods/GetAddressIndonesia)

```bash
  git clone https://github.com/sandrocods/GetAddressIndonesia
  cd GetAddressIndonesia
```

Install requirements.txt
```bash
  pip3 install -r ./requirements.txt
``` 

Run Example
```bash
  python3 main.py
``` 

#### To use automate scrape insert database use [scrapping_data.py](https://github.com/sandrocods/GetAddressIndonesia/blob/master/scrapping_data.py)



## API Reference

#### Get Fresh Data From Pos Indonesia

```python
from GetAddressIndonesia import get_data
get_data(a)

# return list
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `a` | `string` | **Required**. Village, Sub-district, District/regency |

#### Get city or province clean data

```python
from GetAddressIndonesia import get_by
get_by(a)

# return list
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `a` | `string` | **Required**. city/province |



#### Get Data from database

```python
from database import Database
database = Database('data.db')
database.search_multi(a)

# return string json formatted
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `a` | `string` | **Required**. Postal Code, Village, Sub-district, District/regency |

#### Reset all data in database
```python
from database import Database
database = Database('data.db')
database.reset_database()

```
## Running Tests

To run tests, run this script

- [Test Database](https://github.com/sandrocods/GetAddressIndonesia/blob/master/test/test_database.py)
- [Test Request Data](https://github.com/sandrocods/GetAddressIndonesia/blob/master/test/test_request_data.py)

Result : 
- [Result all test](https://htmlpreview.github.io/?https://github.com/sandrocods/GetAddressIndonesia/blob/master/test/Test%20Results%20-%20.html)
## Support

thank you for visiting this repository, if this repository is useful for your project please give a star ⭐️🙏❤️️ 

