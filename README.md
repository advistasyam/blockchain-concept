<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Blockchain-Concept</h3>

  <p align="center">
   A simple blockchain REST API using FLASK
    <br />
    <br />
    <a>Live Site</a>
  </p>
</p>

<br />

### Built With

-   [Python3](https://www.python.org/)
-   [Flask](https://flask.palletsprojects.com/en/2.0.x/)
-   [SHA256 Proof Of Work](https://en.wikipedia.org/wiki/SHA-2)

<br/>

<!-- GETTING STARTED -->

## Getting Started

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/advistasyam/blockchain-concept
    ```
2. Install PyPi packages
    ```sh
    pip install -r requirements.txt
    ```
3. Run Server
    ```sh
    python blockchain.py <PORTNUMBER>
    ```

### Routes

* "/"  Response Example:
    ```json
    {
        "chain": [
            {
                "hash_of_previous_block": "b085f0847895b23e0c565578283e70ea4b39ffc430fbcbbb7227b24e93838961",
                "index": 0,
                "nonce": 112756,
                "timestamp": 1625148147.788609,
                "transaction": []
            },
            {
                "hash_of_previous_block": "4d7ea7f44d7d294a86db91a5f1f59e9d2dcfdab4ad29a76cdbb68f96e7920f86",
                "index": 1,
                "nonce": 6461,
                "timestamp": 1625148205.64302,
                "transaction": [
                    {
                        "amount": 25,
                        "recipient": "bayu",
                        "sender": "adit"
                    },
                    {
                        "amount": 50,
                        "recipient": "dimas",
                        "sender": "caca"
                    },
                    {
                        "amount": 5,
                        "recipient": "89facc696dfa455c89eb2c04dcfc1515",
                        "sender": "0"
                    }
                ]
            }
        ],
        "length": 2
    }
    ```
    
* "/transactions/new", Requested Body: {amount, reciepient, sender}. Response Example :
    ```json
    {
        "message": "Transaksi akan dimasukkan ke blok ke 1"
    }
    ```
* "/mine"
    ```json
    {
        "hash_of_previous_block": "4d7ea7f44d7d294a86db91a5f1f59e9d2dcfdab4ad29a76cdbb68f96e7920f86",
        "index": 1,
        "message": "A new block has been added",
        "nonce": 6461,
        "transactions": [
            {
                "amount": 25,
                "recipient": "bayu",
                "sender": "adit"
            },
            {
                "amount": 50,
                "recipient": "dimas",
                "sender": "caca"
            },
            {
                "amount": 5,
                "recipient": "89facc696dfa455c89eb2c04dcfc1515",
                "sender": "0"
            }
        ]
    }
    ```

## Contributing! ya benar, kalimat dibawah ini template cuy

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch with your name (`git checkout -b yourname/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin yourname/AmazingFeature`)
5. Open a Pull Request