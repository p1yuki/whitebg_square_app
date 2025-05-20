from PIL import Image
import gradio as gr

# 画像1枚を正方形に変換する関数
def make_square_white(image: Image.Image) -> Image.Image:
    w, h = image.size
    size = max(w, h)
    new_img = Image.new("RGB", (size, size), (255, 255, 255))
    new_img.paste(image, ((size - w) // 2, (size - h) // 2))
    return new_img

# 複数画像を一括で処理する関数
def process_images(image_list):
    return [make_square_white(img) for img in image_list]

demo = gr.Interface(
    fn=process_images,
    inputs=gr.File(file_types=["image"], file_count="multiple", label="画像を複数選んでね"),
    outputs=gr.Gallery(label="変換後の画像たち").style(grid=(3, 3)),
    title="複数画像を白背景で正方形に変換するツール",
    description="複数枚の画像をアップロードすると、それぞれ白背景で正方形に整えて表示します。",
)

if __name__ == "__main__":
    demo.launch()
