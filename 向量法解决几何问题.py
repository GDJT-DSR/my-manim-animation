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

        #设置tex宏包
        template = TexTemplate()
        config.tex_template = template
        template.add_to_preamble('\n\\usepackage[d]{esvect}')

        self.draw_picture()
        self.solution()
        

    def draw_picture(self):
        radius = .03

        A = Dot([2.744,2.909,0],radius=radius)
        A_label = Tex('A').next_to(A,UP,.1)
        B = Dot(ORIGIN,radius=radius)
        B_label = Tex('B').next_to(B,LEFT,.1)
        C = Dot(RIGHT*4,radius=radius)
        C_label = Tex('C').next_to(C,RIGHT,.1)
        D = Dot([2,0,0],radius=radius)
        D_label = Tex('D').next_to(D,DOWN,.1)
        E = Dot([1.581,.969,0],radius=radius)
        E_label = Tex('E').next_to(E,LEFT,.1)
        O = Dot([2,.8627,0],radius=radius)
        O_label = Tex('O').next_to(O,DOWN,.1)
        F = Dot([2.248,.969,0],radius=radius)
        F_label = Tex('F').next_to(F,RIGHT,.1)

        AB = draw_line(A,B)
        BC = draw_line(B,C)
        AC = draw_line(A,C)
        AD = draw_line(A,D)
        # DE = line(D,E)
        OE = draw_line(O,E)
        BF = draw_line(B,F)
        EF = draw_line(E,F)

        group = VGroup(A,B,C,D,E,F,O,AB,BC,AC,AD,OE,BF,EF,A_label,B_label,C_label,D_label,E_label,F_label,O_label)
        group.to_edge(RIGHT,.7)
        # self.add(group)

        txt = VGroup(
            Text('在'),
            MathTex(r'\triangle ABC'),
            Text('中，'),
            MathTex("O"),
            Text('为外心，'),
            MathTex('AD'),
            Text('为中线，'),
            MathTex("E"),
            Text('为'),
            MathTex(r"\triangle ABD"),
            Text('的重心，'),#11
            MathTex(r"BO\cap AD=F"),
            Text('，若'),#13
            MathTex(r'OE\perp AD'),
            Text('，证明：'),#15
            MathTex(r' EF\parallel BC.')
        )
        txt.arrange(RIGHT,.1).to_edge(UL,.2)
        # self.add(txt)

        self.play(
            Write(txt[:3]),
            Create(VGroup(A,B,C,A_label,B_label,C_label,AB,BC,AC)),
            run_time=.3
        )
        # self.wait(1)
        self.play(
            Write(txt[3:5]),
            Create(VGroup(O,O_label)),
            run_time=.3
        )
        # self.wait(1)
        self.play(
            Write(txt[5:7]),
            Create(VGroup(D,AD,D_label)),
            run_time=.3
        )
        # self.wait(1)
        self.play(
            Write(txt[7:11]),
            Create(VGroup(E,E_label)),
            run_time=.3
        )
        # self.wait(1)
        self.play(
            Write(txt[11]),
            Create(VGroup(BF,F,F_label)),
            run_time=.3
        )
        # self.wait(1)
        self.play(
            Write(txt[12:15]),
            Create(VGroup(OE)),
            run_time=.3
        )
        # self.wait(1)
        self.play(
            Write(txt[15:]),
            Create(VGroup(EF)),
            run_time=.3
        )

        self.wait(5)
        # self.txt = txt

    def solution(self):
        prefix = Text("证明：").set_color(YELLOW)
        prefix.to_edge(UP,.8).to_edge(LEFT,.2)
        self.play(Create(prefix))
        solution = VGroup(
            line_group(
                Text('设'),
                MathTex(r'\vv{OA}=\vv{a},\vv{OB}=\vv{b},\vv{OC}=\vv{c}'),   
            ),
            line_group(
                Text('则有'),
                MathTex(r'\vv{AD}=',r'\vv{OD}',r'-\vv{OA}')
            ),
            line_group(
                Text('故'),
                MathTex(r'\vv{OE}=',r'\vv{OA}+',r'\vv{AE}',' ',' '),
            ),
            line_group(
                Text('由'),
                MathTex(r'OE\perp AD'),
                Text('得'),
                MathTex(r'\vv{OE}',r'\cdot',r'\vv{AD}','=0'),
            ),
            line_group(
                Text('由点'),
                MathTex('O'),
                Text('为外心，则'),
                MathTex("BO"),
                Text('垂直平分'),
                MathTex("AC"),
                Text('，因此'),
                MathTex('AB=CB')
            ),
            line_group(
                Text('则直线'),
                MathTex(r'OB'),
                Text('是'),
                MathTex(r'\triangle ABC'),
                Text('的中线所在直线，又'),
                MathTex(r'AD'),
                Text('为中线，'),
            ),
            line_group(
                Text('所以点'),
                MathTex('F'),
                Text('是'),
                MathTex(r'\triangle ABC'),
                Text('的重心，'),
                Text('则有'),
                MathTex(r'\vv{AF}=\frac23\vv{AD}')
            ),
            line_group(
                Text('故'),
                MathTex(r'\vv{EF}=',r'\vv{AF}','-',r'\vv{AE}')
            ),
            Text('命题得证！')
        ).arrange(DOWN,.35,aligned_edge=LEFT)
        solution.next_to(prefix,RIGHT,.3,UP)
        self.play(Write(solution[0]))
        self.wait(1)
        self.play(Write(solution[1]))
        self.wait(1)


        origin_tex = solution[1][1]
        target_tex = MathTex(r'\vv{AD}=',r'\frac12(\vv{OB}+\vv{OC})',r'-\vv{OA}')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex=solution[1][1]=target_tex
        self.wait(1)
        target_tex = MathTex(r'\vv{AD}=',r'-\vv{a}+\frac12\vv{b}+\frac12\vv{c}')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex=solution[1][1]=target_tex
        self.wait(1)


        self.play(Write(solution[2]))
        origin_tex = solution[2][1]
        target_tex = MathTex(r'\vv{OE}=',r'\vv{OA}+',r'\frac13\vv{AB}','+',r'\frac13\vv{AD}')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        self.wait(1)
        origin_tex=solution[2][1]=target_tex
        target_tex = MathTex(r'\vv{OE}=',r'\vv{OA}+',r'\frac13(\vv{OB}-\vv{OA})','+',r'\frac13\Big(\!-\vv{a}+\frac12\vv{b}+\frac12\vv{c}\Big)')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex = solution[2][1] = target_tex
        self.wait(1)
        target_tex = MathTex(r'\vv{OE}=',r'\frac13\vv{a}+\frac12\vv{b}+\frac16\vv c')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex = solution[2][1] = target_tex
        self.wait(1)


        self.play(Write(solution[3]))
        self.wait(1)
        origin_tex = solution[3][3]
        target_tex = MathTex(r'\Big(\frac13\vv{a}+\frac12\vv{b}+\frac16\vv c\Big)',r'\cdot',r'\Big(-\vv{a}+\frac12\vv{b}+\frac12\vv{c}\Big)','=0')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        self.wait(1)
        origin_tex=solution[3][3]=target_tex
        target_tex = MathTex(r'\frac{1}{12}\Big(',r'-4\vv{a}^2+3\vv{b}^2+\vv{c}^2-4\vv{a}\cdot\vv{b}+4\vv{b}\cdot\vv{c}','\\Big)','=0')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        self.wait(1)
        origin_tex=solution[3][3]=target_tex
        target_tex = MathTex(r'\frac{1}{3}(',r'-\vv{a}\cdot\vv{b}+\vv{b}\cdot\vv{c}',')','=0')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        self.wait(1)
        origin_tex=solution[3][3]=target_tex
        target_tex = MathTex(r'\frac{1}{3}(',r'(\vv{c}-\vv{a})\cdot\vv{b}',')','=0')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        self.wait(1)
        origin_tex=solution[3][3]=target_tex
        target_tex = MathTex(r'\frac{1}{3}(',r'\vv{AC}\cdot\vv{OB}',')','=0')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        self.wait(1)
        origin_tex=solution[3][3]=target_tex
        addition = VGroup(Text('，即'),MathTex(r'OB\perp AC')).arrange(RIGHT,.1)
        addition.next_to(solution[3],RIGHT,.1)
        self.play(Write(addition))

        self.play(Write(solution[4]))
        self.wait(1)

        self.play(Write(solution[5]))
        self.wait(1)

        self.play(Write(solution[6][:5]))
        self.play(Write(solution[6][5:]))
        self.wait(1)

        self.play(Write(solution[7]))
        origin_tex = solution[7][1]
        target_tex = MathTex(r'\vv{EF}=',r'\frac23\vv{AD}','-',r'\frac13\big(\vv{AB}+\vv{AD}\big)')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex=solution[7][1]=target_tex
        self.wait(1)
        target_tex = MathTex(r'\vv{EF}=',r'\frac13\vv{AD}','-',r'\frac13\vv{AB}')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex=solution[7][1]=target_tex
        self.wait(1)
        target_tex = MathTex(r'\vv{EF}=',r'\frac13\vv{BD}')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex=solution[7][1]=target_tex
        self.wait(1)
        target_tex = MathTex(r'\vv{EF}=',r'\frac16\vv{BC}')
        target_tex.move_to(origin_tex,LEFT)
        self.play(ReplacementTransform(origin_tex,target_tex))
        origin_tex=solution[7][1]=target_tex
        self.wait(1)

        self.play(Write(solution[8]))
        self.wait(10)


'''
文字：
大家好，今天为大家带来的是一道几何题目，​

由于题目中提供很多三角形“心”的条件，所以我们可以尝试使用向量法来解决这个问题。

首先我们设出三个模长相等的向量用于表示其它向量，进而我们就可以利用向量的运算法则来表示向量AD和向量OE，

接下来我们将题目中的垂直条件转化为两个向量的数量积为0，代入之前的结果后并计算，可以得到另一组垂直条件。

现在通过简单的几何知识可以得到三角形ABC是一个等腰三角形，再根据重心的定义我们很容易得出点F是三角形ABC的重心，进而我们可以得到点F是线段AD的三等分点。

最后我们表示向量EF，并发现它与向量BC是平行的，进而命题成立。

其他方法欢迎在评论区与up一起讨论哦，喜欢的话就点个三连吧～

'''