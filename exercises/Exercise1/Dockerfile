FROM python:3.9

WORKDIR /Exercise1

COPY . .

EXPOSE 8081

RUN pip install matplotlib plotly_express pandas numpy dash scikit-learn
CMD ["python", "src/ex1_0_setup.py"]