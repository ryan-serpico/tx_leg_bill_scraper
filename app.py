import requests, bs4, csv, os

os.makedirs('data', exist_ok=True)

def getHouseBills():
    csvFile = open('data/house_bills.csv', 'w')
    writer = csv.writer(csvFile)

    writer.writerow(['Name', 'Link', 'Author', 'Last action', 'Caption'])

    url = 'https://capitol.texas.gov/Reports/Report.aspx?LegSess=87R&ID=housefiled'

    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    bills = soup.select('table')

    for i in range(0, len(bills)):
        billSoup = bills[i].find_all('td')

        billName = billSoup[0].getText()
        billLink = billSoup[0].find('a').get('href')
        billAuthor = billSoup[2].getText()
        billLastAction = billSoup[5].getText()
        billCaption = billSoup[8].getText()

        writer.writerow([billName, billLink, billAuthor, billLastAction, billCaption])


    csvFile.close()
    print('Done!')

def getSenateBills():
    csvFile = open('data/senate_bills.csv', 'w')
    writer = csv.writer(csvFile)

    writer.writerow(['Name', 'Link', 'Author', 'Last action', 'Caption'])

    url = 'https://capitol.texas.gov/Reports/Report.aspx?LegSess=87R&ID=senatefiled'

    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    bills = soup.select('table')

    for i in range(0, len(bills)):
        billSoup = bills[i].find_all('td')

        billName = billSoup[0].getText()
        billLink = billSoup[0].find('a').get('href')
        billAuthor = billSoup[2].getText()
        billLastAction = billSoup[5].getText()
        billCaption = billSoup[8].getText()

        writer.writerow([billName, billLink, billAuthor, billLastAction, billCaption])


    csvFile.close()
    print('Done!')

getHouseBills()
getSenateBills()