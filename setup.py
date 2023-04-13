from setuptools import setup, find_packages
setup(
    name='safezip',
    version='0.0.1',
    description='Zip files securely',
    author='TheTrojanHorse',
    author_email='taseen.bibi@gmail.com',
    url='https://github.com/yourusername/your_package',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'your_command=your_package_name.main:main',
        ],
    },
    install_requires=[
        # Add any dependencies required by your package here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
)

