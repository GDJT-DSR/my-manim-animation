from manim import *

config.tex_template = TexTemplateLibrary.ctex

class MyScene(Scene):
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=29,font="SimSong")
        MathTex.set_default(font_size=29)

        self.introduce()
        self.solve()

    def introduce(self):
        img = ImageMobject("imgs/特殊极值点偏移.png").to_edge(UP, .5) # 此处 opacity 设置兼容性需注意
        self.play(FadeIn(img))
        self.wait(1)
        self.title = Tex(r'设$f(x)=\mathrm{e}^x-x$，实数$a<b$满足$f(a)=f(b)$，求证：$a+b^2<0$.').scale(1.3).set_color(YELLOW)
        self.play(Create(self.title))
        self.wait(2)
        self.play(FadeOut(img),self.title.animate.to_edge(UP, .8))

    def solve(self):
        deter = Tex(r"$f'(x)=\mathrm{e}^x-1$，",r"则$f(x)$在$(-\infty,0)$上单调递减，在$(0,+\infty)$上单调递增，","因此$a<0<b$.")
        deter.arrange(RIGHT,.1,aligned_edge=ORIGIN)
        deter.next_to(self.title, DOWN, .2, aligned_edge=LEFT).to_edge(LEFT, buff=.8)
        self.play(Write(deter))
        self.wait(2)
        analyze = Tex(
            r"$a+b^2<0$",
            r"$\Leftrightarrow a<-b^2$",
            r"$\Leftrightarrow f(a)>f(-b^2)$",
            r"$\Leftrightarrow f(b)>f(-b^2)$",
            r"$\Leftrightarrow \mathrm{e}^b>\mathrm{e}^{-b^2}+b^2+b$"
        )
        analyze.arrange(RIGHT,0.2,aligned_edge=ORIGIN)
        analyze.next_to(deter, DOWN, aligned_edge=LEFT)
        for item in analyze:
            self.play(Write(item))
            self.wait(1)
        inequality = Tex(r"由$f(x)\ge f(0)$即$\mathrm{e}^x-x\ge1$，",r"则有$\mathrm{e}^{x^2}\ge x^2+1$，",r"则$\mathrm{e}^{-x^2}\le \dfrac{1}{x^2+1}$")
        inequality.next_to(analyze, DOWN,.2, aligned_edge=LEFT)
        for pirce in inequality:
            self.play(Write(pirce))
            self.wait(1)
        self.wait(2)

        newq = Tex(r"因此只需要证明：$e^b>b+b^2+\dfrac{1}{b^2+1}$")
        newq.next_to(inequality, DOWN,.2, aligned_edge=LEFT)
        self.play(Write(newq))
        self.wait(2)

        func = VGroup(
            Tex(r"设$g(x)=\Big(x+x^2+\dfrac{1}{x^2+1}\Big)\mathrm{e}^{-x}$"),
            Tex(r"，则$g'(x)=-\dfrac{x(x-1)^2(x^3+x^2+2x+1)}{(x^2+1)^2\mathrm{e}^{x}}\le 0$")
        ).arrange(RIGHT,.2,aligned_edge=ORIGIN)
        func.next_to(newq, DOWN,.2, aligned_edge=LEFT)
        self.play(Write(func[0]))
        self.wait(1)
        self.play(Write(func[1]))
        self.wait(2)

        conclusion =  Tex(r"因此$g(x)$在$(0,+\infty)$上单调递减，则$g(b)<g(0)=1$，则原不等式成立")
        conclusion.next_to(func, DOWN,.2, aligned_edge=LEFT)
        self.play(Write(conclusion))
        self.wait(10)


# 生成视频并预览
with tempconfig({
    # 'quality': 'low_quality',
    'quality': 'high_quality',
    'preview': True,
    'write_to_movie': True
}):
    # 实例化你的场景并开始渲染
    scene = MyScene()
    scene.render()