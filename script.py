import requests
import domesday

def main():
    df = domesday.get_manors_info('dby')
    print(df['geld'].sum())
    print(df['totalploughs'].sum())

if __name__ == "__main__":
    main()