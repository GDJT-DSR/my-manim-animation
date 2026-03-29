from manim import *

def draw_line(start,end,**kwargs):
    return Line(start.get_center(),end.get_center(),**kwargs)

def line_group(*args,**kwargs):
    return VGroup(*args,**kwargs).arrange(RIGHT,.1)


class MyScene(Scene):
    CONFIG = {}
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)
        
        #显示题目
        title = Text('康托洛维奇不等式',color=YELLOW)
        title.to_edge(UP,.2)
        title.scale(1.3)
        desc = VGroup(
            line_group(
                Text('正实数'),
                MathTex(r'x_1,x_2,\ldots,x_n'),
                Text('满足'),
                MathTex(r'x_1+x_2+\cdots+x_n=1'),
                Text('，实数'),
                MathTex(r'a_1,a_2,\ldots,a_n'),
                Text('满足'),
                MathTex(r'0<m\le a_i\le M,i=1,2,\ldots,n'),
                Text('，则')
            ),
            MathTex(r'\Big(\sum_{i=1}^na_ix_i\Big)\Big(\sum_{i=1}^n\frac{x_i}{a_i}\Big)',r'\le',r'\frac{(M+m)^2}{4Mm}'),
        ).arrange(DOWN,.2).next_to(title,DOWN).to_edge(LEFT,.2)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(desc[0]))
        self.play(Write(desc[1]))
        self.wait(4)

        solution = VGroup(
            MathTex(
                r'\mathrm{LHS}=',
                r'\frac{1}{Mm}\Big(\sum_{i=1}^na_ix_i\Big)\Big(\sum_{i=1}^nx_i\cdot\frac{Mm}{a_i}\Big)'
            ),
            MathTex(r'\le',r'\frac{1}{4Mm}\Big(',r'\sum_{i=1}^nx_i',r'\Big(a_i+\frac{Mm}{a_i}\Big)',r'\Big)^2'),
            MathTex(r'\le',r'\frac{1}{4Mm}\Big(',r'\sum_{i=1}^nx_i','(m+n)',r'\Big)^2'),
            MathTex(r'=',r'\frac{1}{4Mm}\Big(','(m+n)',r'\sum_{i=1}^n x_i',r'\Big)^2'),
            MathTex('=',r'\frac{(M+m)^2}{4Mm}')
        ).arrange(DOWN,.1,aligned_edge=LEFT)
        solution.next_to(desc,DOWN,.2).to_edge(LEFT,.4)

        self.play(Write(solution[0]))
        self.wait(1)
        self.play(Write(solution[1]))
        self.wait(1)

        box = SurroundingRectangle(solution[1][3])
        self.play(Create(box))
        self.wait(1)


        #定义内容部分
        # axes = Axes(
        #     x_range=[0, 1.5, .3],
        #     y_range=[0, 1.5, .3],
        #     x_length=4,
        #     y_length=4,
            
        #     axis_config={"color": BLUE,
        #         "tip_width": 0.1,    # 箭头宽度
        #         "tip_height": 0.1,    # 箭头高度
        #         "include_tip": True,  # 包含箭头
        #     }
        # )
        # axes.to_edge(RIGHT, buff=0.7)
        # self.play(Create(axes))

        # plot = axes.plot(lambda x:x+0.24/x,x_range=[0.2,1.2],color=RED)
        # self.play(Create(plot))

        extra = VGroup(
            line_group(
                Text('因为'),
                MathTex(r'0<m\le a_i\le M')
            ),
            line_group(
                Text('所以'),
                MathTex(r'(a_i-m)(a_i-M)\le0'),
            ),
            line_group(
                Text('即'),
                MathTex(r'a_i^2-(M+m)a_i+Mma_i\le0')
            ),
            line_group(
                Text('由'),
                MathTex(r'a_i>0'),
                Text('得到'),
                MathTex(r'a_i+\frac{Mm}{a_i}\le M+m')
            ),
            line_group(
                Text('当且仅当'),
                MathTex(r'a_i=M'),
                Text('或'),
                MathTex(r'a_i=m'),
                Text('时取等'),
            )
        ).arrange(DOWN,.2,aligned_edge=LEFT)
        extra.set_color(YELLOW)
        extra.next_to(solution,RIGHT,1)
        for i in extra:
            self.play(Write(i))
            self.wait(1)

        self.wait(2)

        self.play(Transform(solution[1].copy(),solution[2]),run_time=0.5)
        # self.wait(1)

        self.play(Uncreate(extra),Uncreate(box))
    
        self.wait(1)
        self.play(
            Transform(solution[2][0],solution[3][0]),
            Transform(solution[2][1],solution[3][1]),
            Transform(solution[2][3],solution[3][2]),
            Transform(solution[2][2],solution[3][3]),
            Transform(solution[2][4:],solution[3][4:]),
        )
        self.wait(1)
        self.play(Transform(solution[3][:2],solution[4]))

        self.wait(5)

        equal = VGroup(
            line_group(
                Text('取等时，'),
                MathTex(r'a_i=M'),
                Text('或'),
                MathTex(r'm'),
                Text('且'),
                MathTex(r'\sum_{i=1}^na_ix_i=\sum_{i=1}^nx_i\cdot\frac{Mm}{a_i}')
            ),
            line_group(
                Text('设'),
                MathTex(r's=\sum_{a_i=m}x_i,\;t=\sum_{a_i=M}x_i'),
                Text('，则'),
                MathTex(r's+t=1')
            ),
            line_group(
                Text('由取等知'),
                MathTex(r'ms+Mt=Ms+mt'),
                Text('，即'),
                MathTex(r'(M-m)(s-t)=0'),
            ),
            line_group(
                Text('所以'),
                MathTex(r'M=m'),
                Text('或'),
                MathTex(r's=t=\frac12')
            ),
            Text('即为取等条件')
        ).arrange(DOWN,.2,aligned_edge=LEFT)
        equal.set_color(BLUE)
        equal.next_to(solution,RIGHT,.5,UP)

        for item in equal:
            self.play(Write(item))
            self.wait(1)

        

'''
大家好，今天为大家带来的是康托洛维奇不等式。
它的形式如下：

1s

让我们来尝试证明这个不等式。
首先，对原不等式的左侧进行一步恒等变形以便处理。
接着，直接使用均值不等式将积的形式放缩为和的形式。
此时我们可以使用题目中的大小关系对方框内的项进行一些估计。
4s
我们把它放缩为常数以便利用求和的条件。
3s


进而我们可以将常数提取到和号的外面，然后就可以使用和为1这一条件。
最后我们只需要简单的化简一下就可以得到原不等式的右侧，完成了不等式的证明。

1s

接下来我们来探究取等条件，需要使得两步估计均能取到等，接着我们将不同的ai所对应的xi分别求和，并通过均值不等式的取等条件得到s,t和m的关系，就得到最终的取等条件。
1s
喜欢的话可以给up一个三连吗？

'''