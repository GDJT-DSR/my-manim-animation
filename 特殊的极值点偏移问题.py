from manim import *

class MyScene(Scene):
    def construct(self):
        pass

# 生成视频并预览
with tempconfig({
    'quality': 'low_quality',
    # 'quality': 'high_quality',
    'preview': True,
    'write_to_movie': True
}):
    # 实例化你的场景并开始渲染
    scene = MyScene()
    scene.render()