
def evaluate_results(results: list):
    # TODO: this function should take the raw results input and output the best
    #  height they achieved
    evaluation = []
    for result in results:
        pass
    pass


def score_pole_vault(vaulter_list):

    for vaulter_dict in vaulter_list:
        # get vaulter name
        vault_name = vaulter_dict["name"]
        vault_results = vaulter_dict["results"]


def main():
    test_data = [
        {"name": "Linda", "results": ["XXO", "O", "XXO", "O"]},
        {"name": "Vickie", "results": ["O", "X", "", ""]},
        {"name": "Debbie", "results": ["XXO", "O", "XO", "XXX"]},
        {"name": "Michelle", "results": ["XO", "XO", "XXX", ""]},
        {"name": "Carol", "results": ["XXX", "", "", ""]}
    ]
    score_pole_vault(test_data)


if __name__ == '__main__':
    main()
