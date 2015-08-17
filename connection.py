import yaml_reader
import yaml

fp = "config.yaml"
yf = yaml_reader.yld

data=yf.yaml_loader(fp)
print (data)
