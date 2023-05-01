import time
import board
import busio
import adafruit_mlx90640
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# Thermal Camera Software
# Isaac Flaum 2023
print("Board Pins:")
print(dir(board))

displayio.release_displays()
display_font = terminalio.FONT

spi = busio.SPI(clock=board.SCK,
                MOSI=board.MOSI,
                MISO=board.MISO)
tft_cs = board.A2
tft_dc = board.A1

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)

mlx_90640_i2c_connection = busio.I2C(board.D1, board.D0, frequency=800000)
mlx_90640 = adafruit_mlx90640.MLX90640(mlx_90640_i2c_connection)
mlx_90640.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

flir_ironbow_colors = [0x00000a, 0x00001e, 0x00002a, 0x000032, 0x00003a, 0x000042, 0x00004a, 0x000052, 0x010057, 0x02005c, 0x040061, 0x050065, 0x070069, 0x09006e, 0x0b0073,
                       0x0d0075, 0x0e0077, 0x120079, 0x15007c, 0x19007e, 0x1c0081, 0x200084, 0x240086, 0x280089, 0x2c008a, 0x30008c, 0x34008e, 0x38008f, 0x3b0091, 0x3e0093,
                       0x410094, 0x440095, 0x470096, 0x4a0096, 0x4e0097, 0x510097, 0x540098, 0x580099, 0x5c0099, 0x5f009a, 0x63009b, 0x66009b, 0x6a009b, 0x6d009c, 0x70009c,
                       0x73009d, 0x77009d, 0x7a009d, 0x7e009d, 0x81009d, 0x84009d, 0x87009d, 0x8a009d, 0x8d009d, 0x91009c, 0x95009c, 0x98009b, 0x9b009b, 0x9d009b, 0xa0009b,
                       0xa3009b, 0xa6009a, 0xa8009a, 0xaa0099, 0xad0099, 0xaf0198, 0xb00198, 0xb20197, 0xb40296, 0xb60295, 0xb80395, 0xba0495, 0xbb0593, 0xbd0593, 0xbf0692,
                       0xc00791, 0xc10890, 0xc20a8f, 0xc30b8e, 0xc50c8c, 0xc60e8a, 0xc81088, 0xca1286, 0xcb1385, 0xcc1582, 0xce1780, 0xcf187c, 0xd01a79, 0xd11c76, 0xd21d74,
                       0xd32071, 0xd4226e, 0xd52469, 0xd72665, 0xd82862, 0xda2b5e, 0xdb2e5a, 0xdc2f54, 0xdd314e, 0xde3347, 0xdf3541, 0xe0373a, 0xe03933, 0xe23b2d, 0xe33d26,
                       0xe43f20, 0xe4421c, 0xe54419, 0xe64616, 0xe74814, 0xe84a12, 0xe84c0f, 0xe94d0d, 0xea4f0c, 0xeb510a, 0xeb5309, 0xec5608, 0xec5808, 0xed5a07, 0xee5c06,
                       0xee5d05, 0xef5f04, 0xef6104, 0xf06303, 0xf06503, 0xf16603, 0xf16803, 0xf16a02, 0xf16b02, 0xf26d01, 0xf36f01, 0xf37101, 0xf47300, 0xf47500, 0xf47700,
                       0xf47a00, 0xf57c00, 0xf57f00, 0xf68100, 0xf78300, 0xf78500, 0xf88700, 0xf88800, 0xf88a00, 0xf88c00, 0xf98d00, 0xf98f00, 0xf99100, 0xf99300, 0xfa9500,
                       0xfb9800, 0xfb9a00, 0xfc9d00, 0xfca000, 0xfda200, 0xfda400, 0xfda700, 0xfdaa00, 0xfdac00, 0xfdae00, 0xfeb000, 0xfeb200, 0xfeb400, 0xfeb600, 0xfeb900,
                       0xfeba00, 0xfebc00, 0xfebe00, 0xfec100, 0xfec300, 0xfec500, 0xfec700, 0xfec901, 0xfeca01, 0xfecc02, 0xfece03, 0xfecf04, 0xfed106, 0xfed409, 0xfed60a,
                       0xfed80c, 0xffda0e, 0xffdb10, 0xffdc14, 0xffde19, 0xffdf1e, 0xffe122, 0xffe226, 0xffe42b, 0xffe531, 0xffe638, 0xffe83f, 0xffea46, 0xffeb4d, 0xffed54,
                       0xffee5b, 0xffef63, 0xfff06a, 0xfff172, 0xfff17b, 0xfff285, 0xfff38e, 0xfff496, 0xfff59e, 0xfff5a6, 0xfff6af, 0xfff7b6, 0xfff8bd, 0xfff8c4, 0xfff9ca,
                       0xfffad1, 0xfffbd8, 0xfffcdf, 0xfffde5, 0xfffeeb, 0xfffef1, 0xfffff6]
flir_ironbow_number_of_colors = len(flir_ironbow_colors)
flir_ironbow_palette = displayio.Palette(flir_ironbow_number_of_colors)

for i in range(len(flir_ironbow_colors)):
    flir_ironbow_palette[i] = flir_ironbow_colors[i]


thermal_group = displayio.Group()
display.show(thermal_group)

def render_thermal_bitmap(frame):
    zoom_scale = 5.625
    thermal_data_frame = [0] * 768
    max_temp = max(frame)
    min_temp = min(frame)
    thermal_bitmap = displayio.Bitmap(int(32 * zoom_scale), int(24 * zoom_scale), flir_ironbow_number_of_colors)
    tile_grid = displayio.TileGrid(thermal_bitmap, pixel_shader=flir_ironbow_palette)
    for h in range(24 * zoom_scale):
        for w in range(32 * zoom_scale):
            thermal_palette_val = int((frame[int(h/zoom_scale)*32 + int(w/zoom_scale)] - min_temp) / (max_temp - min_temp) * flir_ironbow_number_of_colors)
            thermal_bitmap[w, h] = thermal_palette_val
    return tile_grid


data_frame = [0] * 768
try:
    while True:
        try:
            mlx_90640.getFrame(data_frame)
            thermal_data_frame = render_thermal_bitmap(data_frame)
            if (len(thermal_group) > 0):
                thermal_group.pop()
            thermal_group.append(thermal_data_frame)
            display.show(thermal_group)
        except ValueError:
            # these happen, no biggie - retry
            continue
except KeyboardInterrupt:
    pass

