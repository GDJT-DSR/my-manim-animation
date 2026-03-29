from manim import *

class MyScene(Scene):
    CONFIG = {
        "TEX_USE_CTEX": True,  # 使用 LaTeX 渲染 MathTex
        "TEX_CJK_CHAR": True,  # 支持 CJK 字符
        "TEX_FONT": "SimSong",  # 设置默认字体为 SimSong
    }

    def construct(self):
        Text.set_default(font_size=20, font="SimSong")
        MathTex.set_default(font_size=27)
        question = self.get_question()
        self.play(Write(question.scale(1.2)), run_time=3)
        self.wait(2)
        # self.play(question.animate.to_corner(UL), run_time=1)
        self.play(
            question.animate.scale(.8).to_corner(UL),
            run_time=1
        )
        self.proof1(question)
        self.proof2(question)
        self.proof3(question)
        
    def get_question(self):
        return VGroup(
            Text('已知正实数'),
            MathTex('a,b'),
            Text('满足'),
            MathTex('a+b=1'),
            Text('，求'),
            MathTex(r'\frac{1}{\sqrt{2+a^2}}+\frac{1}{\sqrt{2+b^2}}'),
            Text('的最大值.')
        ).arrange(RIGHT, buff=0.1).scale(1.3)
    
    def proof1(self,q):
        title = Text("方法一(导数法/琴生不等式)：",color=YELLOW).scale(1.1)
        l1 = VGroup(
            Text("设"),
            MathTex(r"f(x)=\frac{1}{\sqrt{2+x^2}}+\frac{1}{\sqrt{2+(1-x)^2}}\;(x\in(0,1))"),
            Text("，则"),
            MathTex(r"f'(x)=-\frac{x}{(2+x^2)^{3/2}}+\frac{1-x}{(2+(1-x)^2)^{3/2}}"),
        ).arrange(RIGHT, buff=0.1)
        l2 = VGroup(
            Text("设"),
            MathTex(r"g(x)=\frac{x^2}{(2+x^2)^3}\;(x\in(0,1))"),
            Text("，则"),
            MathTex(r"f'(x)=\sqrt{g(1-x)}-\sqrt{g(x)}"),
            Text("且"),
            MathTex(r"g'(x)=\frac{4x(1-x^2)}{(2+x^2)^4}>0"),
        ).arrange(RIGHT, buff=0.1)
        l3 = VGroup(
            Text(r"当"),
            MathTex(r"x\in\left(0,\frac{1}{2}\right)"),
            Text(r"时，"),
            MathTex(r"g(1-x)>g(x)"),
            Text(r"，所以"),
            MathTex(r"f'(x)>0"),
            Text(r"，因此"),
            MathTex(r"f(x)"),
            Text(r"在区间"),
            MathTex(r"\left(0,\frac{1}{2}\right)"),
            Text(r"上单调递增"),
        ).arrange(RIGHT, buff=0.1)
        l4 = VGroup(
            Text(r"当"),
            MathTex(r"x\in\left(\frac{1}{2},1\right)"),
            Text(r"时，"),
            MathTex(r"g(1-x)<g(x)"),
            Text(r"，所以"),
            MathTex(r"f'(x)<0"),
            Text(r"，因此"),
            MathTex(r"f(x)"),
            Text(r"在区间"),
            MathTex(r"\left(\frac{1}{2},1\right)"),
            Text(r"上单调递减"),
        ).arrange(RIGHT, buff=0.1)
        l5 = VGroup(
            Text(r"因此"),
            MathTex(r"f(x)"),
            Text(r"的最大值为"),
            MathTex(r"f\left(\frac{1}{2}\right)=\frac{4}{3}")
        ).arrange(RIGHT, buff=0.1)

        all = VGroup(title, l1, l2, l3, l4, l5).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        all.next_to(q, DOWN, aligned_edge=LEFT, buff=.3)
        self.play(Write(title), run_time=1)
        self.wait(1)
        self.play(Write(l1), run_time=5)
        self.wait(1)
        self.play(Write(l2), run_time=8)
        self.wait(1)
        self.play(Write(l3), run_time=2)
        self.play(Write(l4), run_time=2)
        self.wait(1)
        self.play(Write(l5), run_time=3)
        self.wait(5)
        self.play(FadeOut(all), run_time=1)
        

    

    def proof2(self, q):
        #定义内容部分
        axes = Axes(
            x_range=[0, 2, 1],
            y_range=[0, .8, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE},
        )
        axes.to_edge(RIGHT, buff=0.3)
        f = axes.plot(lambda x: 1 / ((2 + x**2)**0.5), color=RED, x_range=[0, 2])
        f_label = axes.get_graph_label(f, label=MathTex(r"f(x)=\frac{1}{\sqrt{2+x^2}}"), x_val=1.7, direction=DOWN)
        l = axes.plot(lambda x: (5-x)*4/27, color=GREEN, x_range=[0, 2])
        l_label = axes.get_graph_label(l, label=MathTex(r"y=\frac{4}{27}\left(x-\frac12\right)+\frac23"), x_val=.5, direction=UP)
        title = Text("方法二(切线法)：", color=YELLOW).scale(1.1)

        # 需要证明 1/sqrt{2+x^2} \geq -\frac{4x+20}{27}
        l1 = VGroup(
            Text("需要证明"),
            MathTex(r"\frac{1}{\sqrt{2+x^2}} \leq \frac{-4x+20}{27}")
        ).arrange(RIGHT, buff=0.1)
        l2 = VGroup(
            Text("两边平方得"),
            MathTex(r"\frac{1}{2+x^2} \leq \frac{(-4x+20)^2}{729}"),
        ).arrange(RIGHT, buff=0.1)
        l3 = VGroup(
            Text("其等价于"),
            MathTex(r"\frac{1}{729}(16x^4-160x^3+432x^2-320x+71)\ge 0"),
        ).arrange(RIGHT, buff=0.1)
        l4 = VGroup(
            Text("或者等价于"),
            MathTex(r"\frac{1}{729}(2x-1)^2(2x-9-\sqrt{10})(2x-9+\sqrt{10})\ge 0"),
        ).arrange(RIGHT, buff=0.1)
        l5 = Text('这是显然成立的')
        l6 = VGroup(
            Text("因此"),
            MathTex(r"\frac{1}{\sqrt{2+a^2}}+\frac{1}{\sqrt{2+b^2}}\le \frac{4}{3}"),
        ).arrange(RIGHT, buff=0.1)
        l7 = VGroup(
            Text("当且仅当"),
            MathTex(r"a=b=\frac{1}{2}"),
            Text("时取得等号.")
        ).arrange(RIGHT, buff=0.1)
        l1.next_to(title, DOWN, aligned_edge=LEFT, buff=0.2)
        all = VGroup(title,l1,l2,l3,l4,l5,l6,l7).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        all.next_to(q, DOWN, aligned_edge=LEFT, buff=.3)


        #证明2动画部分
        self.play(Write(title), run_time=1)
        self.play(Create(axes), run_time=1)
        self.play(Create(f), run_time=2)
        self.play(Write(f_label), run_time=1)
        self.wait(1)
        self.play(Create(l), run_time=2)
        self.play(Write(l_label), run_time=1)
        self.wait(2)
        self.play(Write(l1), run_time=2)
        self.wait(2)
        self.play(Write(l2), run_time=3)
        self.wait(2)
        self.play(Write(l3), run_time=3)
        self.wait(2)
        self.play(Write(l4), run_time=3)
        self.play(Write(l5), run_time=2)
        self.wait(2)
        self.play(Write(l6), run_time=4)
        self.play(Write(l7), run_time=3)
        self.wait(5)
        self.play(FadeOut(VGroup(all,axes,f, l, f_label, l_label)), run_time=1)

    def proof3(self,q):
        # 标题
        title = Text("方法三(不等式法)：", color=YELLOW).scale(1.1)
        title.next_to(q, DOWN, aligned_edge=LEFT, buff=.3)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # 不等式部分
        l1 = VGroup(
            Text("由"),
            Text('Cauchy-Schwarz',font='Times New Roman'),
            Text("不等式得"),
            MathTex(r"\left(\frac{1}{\sqrt{2+a^2}}+\frac{1}{\sqrt{2+b^2}}\right)^2\le (1+1)\left(\frac{1}{2+a^2}+\frac{1}{2+b^2}\right)")
        ).arrange(RIGHT, buff=0.1)
        l1.next_to(title, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(l1), run_time=3)
        self.wait(2)

        l2 = VGroup(
            Text("不妨设"),
            MathTex(r"a\ge b"),
            Text("，则"),
            MathTex(r"1-2a\le 1-2b"),
            Text("且"),
            MathTex(r"\frac{1+2a}{9(2+a^2)}\ge \frac{1+2b}{9(2+b^2)}"),
            Text("(因为其等价于"),
            MathTex(r"(a-b)(a+b+2ab-4)\le0"), Text(")")
        ).arrange(RIGHT, buff=0.1)
        l2.next_to(l1, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(l2), run_time=5)
        self.wait(2)

        l3 = VGroup(
        Text("由"),
        Text("Chebyshev",font='Times New Roman'),
        Text("不等式得"),
        ).arrange(RIGHT, buff=0.1)
        l3.next_to(l2, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(l3), run_time=1)

        l4 = MathTex(
            r"(1-2a)\left(\frac{1+2a}{9(2+a^2)}\right)+(1-2b)\left(\frac{1+2b}{9(2+b^2)}\right)"
            r"\leq"
            r"\frac12(1-2a+1-2b)\left(\frac{1+2a}{9(2+a^2)}+\frac{1+2b}{9(2+b^2)}\right)=0"
        )
        l4.next_to(l3, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(l4), run_time=5)
        self.wait(2)

        l5 = VGroup(
            Text("因此"),
            MathTex(r"0\ge \frac{1-4a^2}{9(2+a^2)}+\frac{1-4b^2}{9(2+b^2)}=\frac{1}{2+a^2}+\frac{1}{2+b^2}-\frac{8}{9}"),
            Text("，即"),
            MathTex(r"\frac{1}{2+a^2}+\frac{1}{2+b^2}\le \frac{8}{9}"),
        ).arrange(RIGHT, buff=0.1)
        l5.next_to(l4, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(l5), run_time=4)
        self.wait(2)

        l6 = VGroup(
            Text("因此"),
            MathTex(r"\frac{1}{\sqrt{2+a^2}}+\frac{1}{\sqrt{2+b^2}}\le \sqrt{2\times\frac{8}{9}}=\frac{4}{3}"),
            Text("，当且仅当"),
            MathTex(r"a=b=\frac{1}{2}"),
            Text("时取得等号.")
        ).arrange(RIGHT, buff=0.1)
        l6.next_to(l5, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(l6), run_time=4)
        self.wait(5)


        
'''
文案：
大家好
今天的题目是一道求最值的题目
本期视频为大家提供三种解答。

第一种方法是使用导数
将a看作主元后得到一个关于a的函数f(x)
再对其求导得到两部分的和

再构造一个函数g(x)用于比较f'(x)的大小
发现gx单调递增
所以fx在0到二分之一上单调递增
在二分之一到一上单调递减
即可得到f(x)在x=1/2处取得最大值4/3


第二种方法是使用切线法
如图，建立平面直角坐标系后，在其中画出f(x)的图像
并作出f(x)在x=1/2处的切线
观察发现切线在函数上方
所以可以尝试证明该不等式
只需进行如下的恒等变换及配方可以得到

再使用不等式放缩，
并根据条件消去某些等于0的项，
就可以得到最终的结果了，
该式子在a=b=1/2处取等。

第三种方法是使用不等式放缩。
为了消去题目中的根号，
我们不妨先使用柯西不等式去掉式子中的根号，
再由对称性设出条件a大于等于b，
得到两个新的不等式，
再将其作为切比雪夫不等式的条件，
得出变形后的式子与8/9的差小于等于0，即可得到最终所需要的不等式，仍旧是在a=b=1/2处取等。

0
0:00:00,000 --> 0:00:01,000
大家好

1
0:00:01,000 --> 0:00:03,000
今天的题目是一道求最值的题目

2
0:00:03,000 --> 0:00:07,000
本期视频为大家提供三种解答。

3
0:00:7,000 --> 0:00:10,000
第一种方法是使用导数

4
0:00:10,000 --> 0:00:14,000
将a看作主元后得到一个关于a的函数f(x)

5
0:00:14,000 --> 0:00:18,000
再对其求导得到两部分的和

6
0:00:18,000 --> 0:00:21,000
再构造一个函数g(x)用于比较f'(x)的大小

7
0:00:21,000 --> 0:00:23,000
发现g(x)单调递增

8
0:00:23,000 --> 0:00:27,000
所以f(x)在0到1/2上单调递增

9
0:00:27,000 --> 0:00:29,000
在1/2到1上单调递减

11
0:00:36,000 --> 0:00:39,000
即可得到f(x)在x=1/2处取得最大值4/3

12
0:00:39,000 --> 0:00:41,000
第二种方法是使用切线法

13
0:00:42,000 --> 0:00:46,000
如图，建立平面直角坐标系后，在其中画出f(x)的图像

14
0:00:46,000 --> 0:00:50,000
并作出f(x)在x=1/2处的切线

15
0:00:50,000 --> 0:00:53,000
观察发现切线在函数上方

16
0:00:53,000 --> 0:0:55,000
所以可以尝试证明该不等式

17
0:00:55,000 --> 0:01:00,000
只需进行如下的恒等变换及配方可以得到

22
0:01:06,000 --> 0:01:09,000
再使用不等式放缩，

23
0:01:09,000 --> 0:01:12,000
并根据条件消去某些等于0的项，

24
0:01:12,000 --> 0:01:15,000
就可以得到最终的结果了，

25
0:01:15,000 --> 0:01:18,000
该式子在a=b=1/2处取等。

26
0:01:18,000 --> 0:01:21,000


27
0:01:21,000 --> 0:01:24,000
第三种方法是使用不等式放缩。

28
0:01:24,000 --> 0:01:27,000
为了消去题目中的根号，

29
0:01:27,000 --> 0:01:30,000
我们不妨先使用柯西不等式去掉式子中的根号，

30
0:01:30,000 --> 0:01:33,000
再由对称性设出条件a大于等于b，

31
0:01:33,000 --> 0:01:36,000
得到两个新的不等式，

32
0:01:36,000 --> 0:01:39,000
再将其作为切比雪夫不等式的条件，

33
0:01:39,000 --> 0:01:42,000
得出变形后的式子与8/9的差小于等于0，即可得到最终所需要的不等式，仍旧是在a=b=1/2处取等。



'''

