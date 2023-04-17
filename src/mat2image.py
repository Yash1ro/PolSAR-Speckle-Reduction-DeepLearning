import h5py
import numpy as np
from skimage import exposure
from osgeo import gdal

# 读取HDF5文件中的数据
with h5py.File('path/to/polSARpro_output.h5', 'r') as f:
    sar_data = f['ParisExperimentT']

# 提取四个极化通道的数据
hh = sar_data['HH']
hv = sar_data['HV']
vh = sar_data['VH']
vv = sar_data['VV']

# 计算Pauli合成图像的三个通道
red = hh - vv
green = 2 * hv
blue = hh + vv

# 归一化和线性拉伸
red = exposure.rescale_intensity(red, out_range=(0, 255))
green = exposure.rescale_intensity(green, out_range=(0, 255))
blue = exposure.rescale_intensity(blue, out_range=(0, 255))

# 合并三个通道，生成RGB图像
rgb = np.dstack((red, green, blue))

# 保存为TIF或其他支持的图像格式
output_path = 'path/to/pauli-composite.tif'
driver = gdal.GetDriverByName('GTiff')
ds_out = driver.Create(output_path, hh.shape[1], hh.shape[0], 3, gdal.GDT_Byte)
ds_out.SetGeoTransform((0, 1, 0, 0, 0, -1))  # 这里假设图像的地理坐标为(0, 0)，像素大小为1，图像上下翻转
for i in range(3):
    ds_out.GetRasterBand(i+1).WriteArray(rgb[:,:,i])
ds_out.FlushCache()
ds_out = None
