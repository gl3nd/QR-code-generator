import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image

from datetime import datetime

# Generate a timestamp-based version
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


# URL to encode in the QR code
url = "https://github.com/gl3nd"  # Replace with your URL

# Create the QR Code instance with high error correction for logo overlay
qr = qrcode.QRCode(
    version=4,  # Adjust version based on your data/desired size
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Build a styled QR code image:
# - RoundedModuleDrawer gives rounded edges to the modules.
# - RadialGradiantColorMask applies a subtle gradient.
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),       # white background
        center_color=(0, 128, 255)          # vibrant blue center gradient
    )
)

# Load your resume logo image
logo = Image.open("logo.png") 

# Create a new image with a solid background
background = Image.new("RGBA", logo.size, (255, 255, 255, 255))  # White background
background.paste(logo, (0, 0), logo)

# Convert to RGB (removes transparency)
logo = background.convert("RGB")


# Force the logo to be black and white:
# First, convert to grayscale ("L" mode), then back to RGB so it can overlay on a colored QR.
logo = logo.convert("L").convert("RGB")

# Calculate a suitable logo size (e.g., 20% of the QR code's width)
qr_width, qr_height = img.size
logo_size = int(qr_width * 0.2)
logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

# Compute the position to center the logo on the QR code
logo_pos = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)

# Overlay the logo on the QR code.
# If your logo image has transparency (e.g. PNG with alpha), pass it as a mask.
if logo.mode in ('RGBA', 'LA'):
    img.paste(logo, logo_pos, logo)
else:
    img.paste(logo, logo_pos)

# Save with versioning
filename = f"qr_with_logo_{timestamp}.png"
img.save(filename)
print(f"Qr code saved as {filename}")