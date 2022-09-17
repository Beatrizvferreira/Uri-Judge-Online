h_i,m_i,h_f,m_f = input().split()
h_i = int(h_i)
h_f = int(h_f)
m_i = int(m_i)
m_f = int(m_f)

if h_i == h_f and m_i == m_f:
    m=0
    h=24
else:
    if h_i+1 == h_f and m_f<m_i:
        h=0
        m=60-m_i+m_f
    else:
        if h_f == h_i:
            if m_f>m_i:
                h=0 
                m= m_f - m_i
            else:
                h=23
                m=60 - m_i + m_f
        else:
            if h_f > h_i:
                h=h_f - h_i 
            elif h_f < h_i:
                h = 24 - h_i + h_f 
            if m_f > m_i:
                m=m_f - m_i
            elif m_f < m_i:
                m = 60 - m_i + m_f 
                h=h-1
            elif m_f == m_i:
                m = 0

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')