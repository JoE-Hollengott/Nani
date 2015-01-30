from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'nani/VERSION'), 'rb') as f:
	version = f.read().decode('ascii').strip()

setup(
	name='Nani',
	version=version,
	url='',
	description='A Software Development Question & Answer Aggregator',
	long_description=open('README.md').read(),
	author='Daniel Draper',
	author_email='drapstv@gmail.com',
	license='MIT',
	packages=find_packages(exclude=('tests', 'tests.*')),
	include_package_data=True,
	zip_safe=False,
	entry_points={
		'console_scripts': ['nani = nani.cmdline:run']
	},
	classifiers=[
		'Framework :: Nani',
		'Development Status :: 1 - Planning',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: MIT License',
		'Operating System :: Unix',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
		'Topic :: Software Development',
	],
	install_requires=[
		'MechanicalSoup',
	]
)
