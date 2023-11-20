# scraper/scraper.py
import requests
from bs4 import BeautifulSoup
from models.bps_models import DataModel
from config.db_config import create_database_session

def run_scraper():
    url = 'https://bps.go.id/indicator/169/1956/1/-seri-2010-2-pdb-triwulanan-atas-dasar-harga-konstan-menurut-pengeluaran.html'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        datatable = soup.find('tablex', class_='datatable')

        if datatable:
            data = []
            headers = [header.text.strip() for header in datatable.find_all('th')]
            rows = datatable.find_all('tr')[1:]

            for row in rows:
                row_data = [cell.text.strip() for cell in row.find_all('td')]
                data.append(dict(zip(headers, row_data)))

            # Create a database session and store data
            session = create_database_session()
            for item in data:
                database_entry = DataModel(
                    title=item.get('Judul'),  # Replace 'Judul' with the actual column name on the website
                    year=int(item.get('Tahun')),  # Replace 'Tahun' with the actual column name on the website
                    period=item.get('Triwulan'),  # Replace 'Triwulan' with the actual column name on the website
                    value=float(item.get('Nilai'))  # Replace 'Nilai' with the actual column name on the website
                )
                session.add(database_entry)

            session.commit()
            session.close()

            print("Data scraped and stored in the database.")
        else:
            print("No datatable found on the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Call the scraper function
run_scraper()
