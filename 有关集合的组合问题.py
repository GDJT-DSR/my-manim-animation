from manim import *

class MyScene(Scene):
    def construct(self):
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)
        question = self.getquetion()
        self.play(Write(question),run_time=3)
        self.wait(2)
        self.play(question.animate.to_corner(UL), run_time=1)
        analyze = self.analyze()
        analyze.next_to(question, DOWN, aligned_edge=LEFT, buff=1)
        self.play(Write(analyze[0]), run_time=1)
        self.wait(1)
        self.play(Write(analyze[1]), run_time=4)
        self.wait(2)
        self.play(Write(analyze[2]), run_time=3)   
        self.wait(5)
        self.play(FadeOut(analyze), run_time=1)

        prf1 = self.prf1()
        prf1.next_to(question, DOWN, aligned_edge=LEFT, buff=1)
        self.play(Write(prf1[0]), run_time=1)
        self.wait(1)
        self.play(Write(prf1[1]), run_time=7)
        self.wait(1)
        self.play(Write(prf1[2]), run_time=1)
        self.wait(1)

        self.play(FadeOut(prf1), run_time=1)
        prf2 = self.prf2()
        prf2.next_to(question, DOWN, aligned_edge=LEFT, buff=1)
        self.play(Write(prf2[0]), run_time=1)
        self.wait(1)
        self.play(Write(prf2[1]), run_time=6)
        self.wait(1)
        self.play(Write(prf2[2]), run_time=1)
        self.wait(5)


        

    def getquetion(self):
        line1 = VGroup(
            Text('求最小的正整数' ),
            MathTex(r'n\;(n\ge 5)'),
            Text('，使得对任意' ),
            MathTex('\\{a,b,c,d,e\}\\subseteq\\{1,2,\\ldots,n\\}'),
        )
        line2 = VGroup(
            Text('均存在正整数' ),
            MathTex('t(1\\le t\\le n-1)'),
            Text('，使得' ),
            MathTex('a,b,c,d,e,a+t,b+t,c+t,d+t,e+t'),
            Text('两两不同.' )
        )
        line1.arrange(RIGHT,aligned_edge=DOWN,buff=0.1)
        line2.arrange(RIGHT,aligned_edge=DOWN,buff=0.1)
        return VGroup(line1,line2).arrange(DOWN,aligned_edge=LEFT)
    
    def analyze(self):
        """
        分析问题函数：
        1. 最小值定义：要求最小的正整数 n (n >= 5)，满足下述条件。
        2. 条件描述：对于任意从 {1,2,...,n} 中选出的 5 个不同元素 a,b,c,d,e，
           必须存在正整数 t (1 <= t <= n-1)，使得集合 {a, b, c, d, e, a+t, b+t, c+t, d+t, e+t}
           中的 10 个数两两不同（加法在模 n 意义下进行）。
        3. 思路分析：
           - 枚举 n，从 5 开始递增。
           - 对于每个 n，枚举所有 5 元子集 {a,b,c,d,e}。
           - 对每个子集，检查是否存在 t 满足上述条件。
           - 如果所有子集都存在这样的 t，则该 n 满足条件，返回最小的 n。
        4. 关键点：
           - “最小”指找到第一个满足条件的 n。
           - “存在 t”是存在性条件，不要求唯一。
           - “两两不同”要求集合中没有重复元素。
        """
        txt = Text('分析：',color=YELLOW).scale(1.2)
        minAnalyze = VGroup(
            VGroup(Text('设最小值为'),MathTex('N'),Text('，则其等价于以下两个条件同时成立：')).arrange(RIGHT, aligned_edge=DOWN, buff=0.2),
            VGroup(
                Text(' (1)'),
                MathTex(r'n\ge N'),
                Text('，或者等价于'),
                MathTex(r'n< N'),
                Text('时一定不成立；')
            ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2),
            VGroup(
                Text(' (2)'),
                MathTex(r'n=N'),
                Text('时成立'),
            ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        differAnalyze = VGroup(
            Text('10个数两两不同等价于'),
            MathTex('t'),
            Text('一定不是某两个数的差.')
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        return VGroup(txt,minAnalyze,differAnalyze).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        

    def prf1(self):
        def instance(n,b,c,d):
            return VGroup(
                MathTex('n=',str(n)),
                Text('时，令'),
                MathTex('a=1',',b=',str(b),',c=',str(c),',d=',str(d),',e=',str(n)),
                Text('，经检验此时不存在满足条件的数'),
                MathTex('t')
            ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        subtitle = Text('(1)的证明：', color=YELLOW).scale(1.2)
        prf = VGroup(
            instance(5,2,3,4),
            instance(6,2,4,5),
            instance(7,2,4,6),
            instance(8,2,4,6),
            instance(9,2,4,8),
            instance(10,2,5,8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        conclusion = VGroup(
            Text('因此，'),
            MathTex('n\ge11'),
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)

        return VGroup(subtitle, prf,conclusion).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
    
    def prf2(self):
        # 证明 (2) 的函数
        subtitle = Text('(2)的证明：', color=YELLOW).scale(1.2)
        line1 = VGroup(
            MathTex('n=11'),
            Text('时，假设可以找到五个数'),
            MathTex('a,b,c,d,e\\;(a<b<c<d<e),'),

        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line11 = VGroup(
            Text('满足对任意正整数正整数'),
            MathTex('t\\;(1\\le t\\le 10)'),
            Text('，均有'),
            MathTex('a+t,b+t,c+t,d+t,e+t'),
            Text('有相同项'),).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line2 = VGroup(
            Text('考虑所有可能的两个数的差，分别为'),
            MathTex('b-a, c-a, d-a, e-a, c-b, d-b, e-b, d-c, e-c, e-d'),
            Text('共10个'),
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line3 = VGroup(
            Text('由于1-10中所有的差值均在这10个数中，'),
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line31 = VGroup(
            Text('因此'),
            MathTex(r'\{1,2,\ldots,10\}=\{b-a, c-a, d-a, e-a, c-b, d-b, e-b, d-c, e-c, e-d\}'),
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line4 = VGroup(
            Text('所以'),
            MathTex(r'1+2+\cdots+10=(b-a)+(c-a)+(d-a)+\cdots+(e-d)'),
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line5 = VGroup(
            Text('即'),
            MathTex('55=2(2e+d-b-2a)'),
            Text('，但左边为奇数，右边为偶数，所以假设不成立.')
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        line6 = VGroup(
            Text('因此'),
            MathTex('n=11'),
            Text('时满足题设条件')
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        prf = VGroup(line1,line11, line2, line3,line31,line4,line5,line6).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        conclusion = VGroup(
            Text('综上所述，所求最小的正整数为'),
            MathTex('n=11'),
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)

        return VGroup(subtitle, prf, conclusion).arrange(DOWN, aligned_edge=LEFT, buff=0.4)