def get_categorical_variables(df):
  return [var for var in df if df[var].dtypes == object]

def get_numerical_variables(df):  
  return [var for var in df if df[var].dtypes != object]

def in_range(col, min_val, max_val):
  return (col >= min_val) & (col <= max_val)