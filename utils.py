def get_categorical_variables(df):
  return [var for var in df if df[var].dtypes == object]

def get_numerical_variables(df):  
  return [var for var in df if df[var].dtypes != object]