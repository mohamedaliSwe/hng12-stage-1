# HNG12 STAGE 1

This is an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Set Up

To run this project locally

### Prerequisites

Ensure that you have python 3 install. you can verify by running.

```bash
python3 --version
```

### Installation

1. Clone the project repository.

```bash
git clone https://github.com/mohamedaliSwe/hng12-stage-1.git
cd hng12-stage-1
```

2. Create a virtual environment and activate it.

- If you are on linux do the following:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

- If you are using windows do the following:

```bash
python -m venv myenv
venv\Scripts\activate
```

3. Intall the required dependencies.

```bash
pip install -r rquirements.txt
```

4. Run the application.

```bash
python3 app.py
```

## API Documentation

### Endpoint

- GET** https://hng12-stage-1.vercel.app/api/classify-number?number=371

### Response format

A successful request will return the following JSON response:

```bash
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

If a request has failed the following response will be returned:

```bash
{
    "number": "alphabet",
    "error": true
}
```

### Usage

To use the API, send a GET request to the deployed endpoint.

```bash
curl https://hng12-stage-1.vercel.app/api/classify-number?number=371
```

## Backlinks

https://hng.tech/hire/python-developers

## License

This project is licensed under the MIT License
