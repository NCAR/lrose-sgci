import io
import os

from airavata_django_portal_sdk import user_storage


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GaussianEigenvaluesViewProvider:
    display_type = 'image'
    name = "Nexrad Display"

    def generate_data(self, request, experiment_output, experiment, output_file=None, output_dir=None, field='DBZ', **kwargs):
            
            data_product_uris = experiment_output.value.split(",")
            
            # Getting all data products
            for i in data_product_uris:
                data_product = request.airavata_client.getDataProduct(request.authz_token, i)
                
                if field is not None:
                    file_name = data_product.productName
                    # for testing
                    print(file_name)
                    print(field)

                    image_file = user_storage.open_file(request, data_product)

                    # If field value is in the file name then display that file
                    if field in image_file.name:
                        print(experiment_output.value)
                        image_bytes = image_file.read()
                        
                # return dictionary with image data
                        return {
                            'image': image_bytes,
                            'mime-type': 'image/png',
                            'interactive': [
                                {'name': 'field',
                                'value': field,
                                'options': [('DBZ', 'DBZ'), ('PHIDP', 'PHIDP'), ('RHOHV', 'RHOHV'), ('VEL', 'VEL'), ('WIDTH', 'WIDTH'), ('ZDR', 'ZDR')],
                                'label': 'Radar data field',
                                'help': 'Change data field to display.'}
                            ]
                        }

