from setuptools import setup,find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Clean folder to arrange your folder',
      author='Oleksand Yukha',
      author_email='filin.gmail@com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder = clean_folder.clean:start']}
      )