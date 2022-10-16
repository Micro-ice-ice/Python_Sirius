import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lab5',
    version='0.1.1',
    author='Drozdov Andrei',
    author_email='andrei.drozdov1@mail.ru',
    description='lab 5',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.sirius-web.org/python-students-22/drozdov_libs',
    packages=['prime_num', 'regular_exp', 'rocket_attack'],
    entry_points={
        'console_scripts': ['prime_num=primes_num.program:prime_num',
                            'rocket_attack=rocket_attack.program:rocket_attack',
                            'regular_exp=regular_exp.program:regular_exp'
                            ],
    },
    install_requires=[],
)
