
class Configuration:
    def __init__(self):
        self.data_path = "C:/Users/pmarc/PycharmProjects/covid19-forecast-hub-europe/data-truth/JHU/"
        self.cols = ["cases"]
        self.target_cols = ["cases"]
        self.input_width = 5
        self.label_width = 1  # Number of days to predict
        self.shift = 1
        self.stride = 1
        self.batch_size = 10
        self.train_data_pcnt = 70
        self.valid_data_pcnt = 20
        self.test_data_pcnt = 10
        self.epochs = 1000
        self.steps_per_epoch = 50
        self.validation_steps = 20
        self.patience = 10
        self.checkpoint_path = "Models/Checkpoints/"
        self.final_model_path = "Models/Final/"
        self.results_path = "Models/Results/"
        self.graphs_path = "Models/Graphs/"
        self.processed_path = "C:/Users/pmarc/PycharmProjects/covid19-forecast-hub-europe/data-processed/UNED-CovidPredPMA/"
        self.is_model_custom_name = False
        self.model_custom_name = "model.h5"
        self.display_images = True
        self.save_images = False
        self.shuffle = False
        self.period = "weeks"
        self.last_day = "2021-05-04"
        self.first_day = "2020-01-23"
        self.predictions_date_init = "2021-09-12"
        self.predictions_date_end = "2021-09-19"
        self.team_model_name = "UNED-CovidPredPMA"
        self.countries = [
            'Austria',
            # 'Belgium',
            # 'Bulgaria',
            # 'Croatia',
            # 'Cyprus',
            # 'Czechia',
            # 'Denmark',
            # 'Estonia',
            # 'Finland',
            # 'France',
            # 'Germany',
            # 'Greece',
            # 'Hungary',
            # 'Iceland',
            # 'Ireland',
            # 'Italy',
            # 'Latvia',
            # 'Liechtenstein',
            # 'Lithuania',
            # 'Luxembourg',
            # 'Malta',
            # 'Netherlands',
            # 'Norway',
            # 'Poland',
            # 'Portugal',
            # 'Romania',
            # 'Slovakia',
            # 'Slovenia',
            # 'Spain',
            # 'Sweden',
            # 'Switzerland',
            # 'United Kingdom'
        ]
        self.country_codes = {
            'Austria': 'AT',
            'Belgium': 'BE',
            'Bulgaria': 'BG',
            'Croatia': 'HR',
            'Cyprus': 'CY',
            'Czechia': 'CZ',
            'Denmark': 'DK',
            'Estonia': 'EE',
            'Finland': 'FI',
            'France': 'FR',
            'Germany': 'DE',
            'Greece': 'GR',
            'Hungary': 'HU',
            'Iceland': 'IS',
            'Ireland': 'IE',
            'Italy': 'IT',
            'Latvia': 'LV',
            'Liechtenstein': 'LI',
            'Lithuania': 'LT',
            'Luxembourg': 'LU',
            'Malta': 'MT',
            'Netherlands': 'NL',
            'Norway': 'NO',
            'Poland': 'PL',
            'Portugal': 'PT',
            'Romania': 'RO',
            'Slovakia': 'SK',
            'Slovenia': 'SI',
            'Spain': 'ES',
            'Sweden': 'SE',
            'Switzerland': 'CH',
            'United Kingdom': 'GB',
        }

