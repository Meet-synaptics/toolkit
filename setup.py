from setuptools import setup, find_packages
import os

def get_requirements(directory):
    requirements = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("requirements.txt"):
                with open(os.path.join(root, file), "r") as f:
                    requirements.extend(f.read().splitlines())
    return requirements

requirements = get_requirements('.')

setup(
    name='toolkit',
    version='3.1.0', #TODO: Automate versioning
    author='Synaptics',
    author_email='meetdineshbhai.patel@synaptics.com',
    description='Synaptics AI Toolkit',
    packages=find_packages(),
    python_requires='==3.10.*',
    install_requires=requirements,
    package_data={
        'toolkit': ['*'],
        'pysynap': ['*'],
        'toolkit-prebuilts':['*'],
    },dependency_links=[
        'https://download.pytorch.org/whl/cpu'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'synap_convert=toolkit.synap_convert:main',
            'image_od=toolkit.image_od:main',
            'image_to_raw=toolkit.image_to_raw:main',
            # 'image_from_raw=image_from_raw:main'
            # 'encrypt-model-ebg=encrypt-model-ebg:main'
        ],
    },
)