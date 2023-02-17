# Add new items to a DynamoDB table

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.batch_write_item(
    RequestItems = {
        "SuperBowl":  [
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "XLVIII",
                        },
                        "date": {
                            "S": "Feb. 2, 2014",
                        },
                        "site": {
                            "S": "MetLife Stadium (East Rutherford, N.J.)",
                        },
                        "result": {
                            "S": "Seattle 43, Denver 8",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "XLIX",
                        },
                       "date": {
                            "S": "Feb. 1, 2015",
                        },
                        "site": {
                            "S": "University of Phoenix Stadium (Glendale, Ariz.)",
                        },
                        "result": {
                            "S": "New England 28, Seattle 24",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "L",
                        },
                       "date": {
                            "S": "Feb. 7, 2016",
                        },
                        "site": {
                            "S": "Levis Stadium (Santa Clara, Calif.)",
                        },
                        "result": {
                            "S": "Denver 24, Carolina 10",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LI",
                        },
                       "date": {
                            "S": "Feb. 5, 2017",
                        },
                        "site": {
                            "S": "NRG Stadium (Houston)",
                        },
                        "result": {
                            "S": "New England 34, Atlanta 28",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LII",
                        },
                       "date": {
                            "S": "Feb. 4, 2018",
                        },
                        "site": {
                            "S": "U.S. Bank Stadium (Minneapolis)",
                        },
                        "result": {
                            "S": "Philadelphia 41, New England 33",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LIII",
                        },
                       "date": {
                            "S": "Feb. 3, 2019",
                        },
                        "site": {
                            "S": "Mercedes-Benz Stadium (Atlanta)",
                        },
                        "result": {
                            "S": "New England 13, Los Angeles Rams 3",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LIV",
                        },
                       "date": {
                            "S": "Feb. 2, 2020",
                        },
                        "site": {
                            "S": "Hard Rock Stadium (Miami)",
                        },
                        "result": {
                            "S": "Kansas City 31, San Francisco 20",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LV",
                        },
                       "date": {
                            "S": "Feb. 7, 2021",
                        },
                        "site": {
                            "S": "Raymond James Stadium (Tampa, Fla.)",
                        },
                        "result": {
                            "S": "Tampa Bay 31, Kansas City 9",
                        },
                    },
                },
            },
             {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LVI",
                        },
                       "date": {
                            "S": "Feb. 13, 2022",
                        },
                        "site": {
                            "S": "SoFi Stadium (Inglewood, Calif.)",
                        },
                        "result": {
                            "S": "Los Angeles Rams 23, Cincinnati 20",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "numero": {
                            "S": "LVII",
                        },
                       "date": {
                            "S": "Feb. 12, 2023",
                        },
                        "site": {
                            "S": "State Farm Stadium (Glendale, Ariz.)",
                        },
                        "result": {
                            "S": "Kansas City 38, Philadelphia 35",
                        },
                    },
                },
            },
        ],
    },
)

print(response)
