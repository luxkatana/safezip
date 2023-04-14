from setuptools import setup, find_packages
setup(
    name='safezip',
    version='0.0.1',
    description='Zip files securely',
    author='TheTrojanHorse',
    author_email='taseen.bibi@gmail.com',
    url='https://github.com/luxkatana/safezip',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'safezip=mainsafezipmod.safezipping',
        ],
    },
    install_requires=[
        'click'
    ],
)

