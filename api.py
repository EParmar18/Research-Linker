import ads
import json
ADS_DEV_KEY = 'CY3aZ8lY2kkFvk3qrUoFICHpP1yHl6IS7dmwmohv'

def main():

    with open( 'papers.json', 'w' ) as f:
        ads.config.token = ADS_DEV_KEY
        papers = ads.SearchQuery( q ="rocket science", sort='citation_count', fl=['title','citation_count','year','author'])

        foundPapers = []

        for paper in papers:
            print(paper.title)
            foundPapers.append( { 'title':str(paper.title),'count':str(paper.citation_count), 'year':str( paper.year ) } )


    with open( 'papers.json', 'w' ) as f:
        json.dump( foundPapers, f )


if __name__== "__main__":
        main()
