import speedtest   
# Speed test
st = speedtest.Speedtest()
 
# Download Speed
ds = st.download()
up = st.upload()
def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
 
#Readable
print(humansize(ds))
print(humansize(up))