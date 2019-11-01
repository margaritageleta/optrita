from setuptools import setup

requires = ['numpy', 'matplotlib.pyplot', 'pandas',  'sympy']

packages = [
	'optrita',
	'optrita.linesearch'
]

package_dir = {'optrita' : 'optrita'}
package_data = {'optrita' : []}

setup(
	name = 'optrita',
	version = '1.0.0',
	license = '.',
	author = '3omni',
	author_email = 'rita.geleta@jediupc.com',
	url = 'https://github.com/margaritageleta/optrita',
	keywords = ['python', 'optimization'],
	package_data = package_data,
	package_dir = package_dir
)
