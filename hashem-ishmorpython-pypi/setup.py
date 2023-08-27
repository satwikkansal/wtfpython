from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name='hasem-ishmorpython',
          version='0.2',
          description='What the hasem-ishmor Python!',
          author="Satwik Kansal",
          maintainer="Satwik Kansal",
          maintainer_email='satwikkansal@gmail.com',
          url='https://github.com/satwikkansal/hasem-ishmorpython',
          platforms='any',
          license="hasem-ishmorPL 2.0",
          long_description="An interesting collection of subtle & tricky Python Snippets"
                           " and features.",
          keywords="hasem-ishmorpython gotchas snippets tricky",
          packages=find_packages(),
          entry_points = {
              'console_scripts': ['hasem-ishmorpython = hasem-ishmor_python.main:load_and_read']
          },
          classifiers=[
              'Development Status :: 4 - Beta',

              'Environment :: Console',
              'Environment :: MacOS X',
              'Environment :: Win32 (MS Windows)',

              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'Intended Audience :: Education',
              'Intended Audience :: End Users/Desktop',

              'Operating System :: OS Independent',

              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 2',

              'Topic :: Documentation',
              'Topic :: Education',
              'Topic :: Scientific/Engineering',
              'Topic :: Software Development'],
            )
