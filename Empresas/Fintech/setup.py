from setuptools import setup, find_packages

setup(
    name="fintech_risk_engine",
    version="0.1.0",
    author="Victor Marques",
    author_email="email.diferente.victor@gmail.com",
    description="Simulador de Análise de Risco de Crédito para Fintechs.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/fintech-risk-engine",

    # Define onde o código fonte está localizado
    package_dir={"": "src"},
    packages=find_packages(where="src"),

    # Dependências do projeto (caso venha a usar pandas, numpy, etc.)
    install_requires=[
        # Exemplo: "pandas>=1.3.0",
    ],

    # Classificadores ajudam as pessoas a encontrar seu projeto no PyPI
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',

    # Cria um comando que pode ser executado diretamente no terminal
    entry_points={
        'console_scripts': [
            'analise-risco=app:run',
        ],
    },
)
