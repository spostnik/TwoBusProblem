#==============================
### bus comes every 20 minutes
### what is mean time of waiting?
# assuming uniform probability density of a bus to arrive 
T = 20.0 #minutes
# using continuous approach
# probability desity by time, normilized
dpOdt = 1.0/T
# <waiting> = {integral 0...T}(t*dpOdt){dt}
mean_wait =(1/T)*(T**2/2.0)
#answer
assert mean_wait==10.0 #mintutes

#using time descretization and taking limit (N -> inf)
# let N to be equal time cells in T, that is, dt=T/(N+1), 
# i=0...N, t = i*dt , thus dt -> 0
# probability to wait i cells of time is the same = 1/(N+1)
# <waiting> = {sum i=0...N}(i*dt)*(1/(N+1))
# geometrical {sum i=0..N} i = N*(N+1)/2
# thus <waiting> = dt*N/2= (T-dt)/2 -> T/2
mean_wait = T/2.0
assert mean_wait==10.0 #mintutes

#==============================
### one bus comes every 20 minutes while another bus comes every 30 minues
### what is mean time of waiting any of them?
T2 = 20.0 #minutes
T3 = 30.0 #minutes
# using continuous approach
# probability desity by time, for each bus
dpOdt2 = 1.0/T2
dpOdt3 = 1.0/T3
# for idependent events we multiply and add alternatives
# {probability that one bus doesn't arrive during t}x{probability of arrival of other} plus vice versa
# probability of waiting time t = 0...T2 (T2<T3)
# after integation over constant value one gets t*dpOdt
# dpOdt = (1-t*dpOdt2)*dpOdt3 + (1-t*dpOdt3)*dpOdt2 = (T2+T3-2*t)/(T2*T3)

# <waiting> = {integral 0...T2}(t*dpOdt){dt} = ((T2+T3)*T2**2/2-2*T2**3/3)/(T2*T3)
mean_wait = T2*(7/18.0)
assert mean_wait==20.0*(7/18.0) # 7.777... mintutes (7+7/9)

#using time descretization and taking limit (N -> inf)
# let it N to be equal time cells in T3, e.g dt=T3/(N+1), 
# i=0...N, t = i*dt
# T2=M*dt and thus M = (N+1)*(T2/T3)
# counting bins of waiting time from cells gives probability of waiting t
# p(t=i*dt)= ((M+N-2*i)/(M*(N+1)))
# <waiting> = {sum i=0...M-1}(i*dt)*p(t=i*dt)
# multimplying numerator and denominator by dt gives
# p(t=i*dt)= ((T2+T3-2*t-dt)/(T2*T3))
# taking N->inf, thus dt->0
# dpOdt -> ((T2+T3-2*t)/(T2*T3))
# arriving to the same formula as above
