FROM python:3.9

WORKDIR /00

ADD ./src/pip_packages.sh .
ADD ./src/ex1_0_setup.py .
ADD ./src/ex1_1_setup.py .

EXPOSE 8081

# RUN pip install numpy pandas matplotlib dash plotly_express scikit-learn
CMD ["/bin/bash", "pip_packages.sh"]