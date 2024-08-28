css = '''
<style>
.chat-container {
    max-width: 800px;
    margin: 0 auto;
}

.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    flex-shrink: 0;
    width: 78px;
    height: 78px;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    flex-grow: 1;
    padding-left: 1.5rem;
    color: #fff;
    word-wrap: break-word;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQAtgMBEQACEQEDEQH/xAAbAAACAgMBAAAAAAAAAAAAAAAAAQUHAgMGBP/EAEMQAAIBAgIECAkKBgMBAAAAAAABAgMEBREGEyExEhRBUVJTkZIHImJxdIGxssEVFjI0NkJVYXKhIzM1VHPRouHwJP/EABsBAQEAAwEBAQAAAAAAAAAAAAABAwQFBgIH/8QANhEBAAIBAgIHBgQFBQAAAAAAAAECAwQRElEFEyExMnGxFBUzQVKBIjRhwVNyodHhI0KR8PH/2gAMAwEAAhEDEQA/ALxAAAAAAPDjtSdHBb+rTeU4W9SUXzNReR9443vHm+Ms7UlRS3JfkdxxFl+DPDKEMJniMop3FepKEZPfCMXlkvWm+w5msvM34HS0dI4ON2sqcZwlGcVKMlk01sa5jT7u1uTG8bKT0rw+nhePXVpbrKipcKC6KazyOxgvN8cTLj5qcF5iEQzKxAKRAgoIEwqb0KvJ2Wk9hOL8WrU1M1zqWxfvkYs9Ytjllw2mt4Xccl1QAAAAAAAAAAAABHaRf0DEvRavus+8Xjr5seX4cqN/0dxxYdboPpVSwWNSyv1LitSfDhUis3Tk9+a5tnIaepwTk/FXvbmmzxj/AA27nY3+m+B2tu6lO7jczy8WnRWbb/PmNSumyWnaYbVtTjrG8SqjE76tiV/XvLnJVa03JxW5fkvMdOlYpWKw5t7cdps8p9PkiBBQQJhSAktGvtFhfpdP3kY8vgnylkx+OF8HIdYAAAAAAAAAAAAAR2kX9AxL0Wr7rPvH46+bHl8EqMR3HGgAYnyAKQCZFBAgpAAVJaNfaLC/S6fvIx5PBPlL7xeOF8HIdYAAAAAAAAALMBOpBPJzin5xsm5ayn049o2XdhXVCvRnRrcCdOpFxnFtZNPeixvHak7TGyI+bGjr34ZZd1GTrsvNi6jFyHzY0c/DLPuoddl5nU4uQ+bGjn4ZZ91DrsvM6nHyHzX0c/DLPuoddl5nU4+Q+a+jn4ZZ91DrsvNepx8ld+EGxssPxqnRw+hTo0tQpONPdnm9pvae1rU7WjqK1rfscubDBBAAUmQSWjX2jwv0un7yPjL4J8pZMXjhetavToJOrLgpvJbDhZtRiwRFsk7RLr1pa87Q0/KFr1q7Ga3vPSfX6snUZORq/tW8tcvWmWOktJM7ccJ1GTk3QqQqLOElJc6NumSl43rO7HNZjvZZn2hgJvJZgQGlGlFpgVJQktbdzWcKKe5c8nyIz4dPbL5MGbPGPzVrimk+MYlJ668nTpvdSotwiuza/XmdKmnxU7oc62fJfvlEOrUbzdSef6mZdoY95GsqdZPvMm0G8k6tTrJ95jaDeS1tTrJ95jaCJktZU6yfeY2g3ktZU6yfeZOxd5GtqdZPvE2g3J1anWT7zC7sZScn4zb87zAxAApMgQElo19pMK9Lp+8jHl8E/d94vHC6Ma/k0/1/A8d038Knn+0vQaXxSiWec3dBiyDOlVqUZcKnJxZlxZsmG3FjnaXzakXjaybsLxXMcnkqkd6+J6rQa6uprtPZaO+HNzYZxz+j2HQYUbj+KwwfC615VybgsoR6UnuR94qTktFYY8uSMdZtKlby6r3t1Uuruo6lao+FKT/9u5Dt1rFa8MONaZtPFLQUIgMwMcyACkQIKCBMKQAFIgQAFSWjP2kwr0un7yMeXwT933i8cLoxr+TT/X8Dx3Tnwqef7S7+k8Uohnm3QIKCDKhVlQrRqQ3xM2nzWw5IyV+T5vSL1msulpVFVhGcXmpLNHt8eSMlIvXulx7RNZ2lW/hRxB1b21w+EvEox1s15T2LsXtOpoqbRNnN1l97RVw7N5pkQAGJABSIEFBAgpAAUiBAAlSZBL6H0pV9KcLguS4UvMo+N8DHmnbHLJijfJC48af8Gl+v4HjunPhU8/2l39J4pRLPOOgRAgpATWB1eHbyg/uPZ5j1HQ2XjwTSflPq5urrtffmqXS66d1pLiE+SNV015o7PgexwV4cdYedz23yyhzKxEwEyACkyBBQQIKQAFJkCAGFYsgALA8FeDTncVcYrQapwTpUM19Jv6T9Rp6q/ZwNzS07eN2mM1M61OC3RTb9Z43prJvkrTl+/wD47ekrtEyjziNwmFIBASOB1ODcVIcjhn2P/s7PQuTbNavON/6/5amrrvSJ/VT1/U1l/dVHvnXqS7ZNn6JWNqxH6PJW8Uy0NlRiyACkQIKOTPkIbFJpb2l5y7Sbww1tPpx7SLvA1kOnHtBvBa2n049pDeC1kOnHtBvA1sOnHtC7wTqQy+nHtIbw9FlZ3V/JRsbatcN9VByXatiPmbRHfL6isz3Q7XR3wdXNxUhXxueooJ5u3g85z/Jvcl5tvmNXJqY7qNnHpp77LIyoWFpGFOEadKnHgwhHYl+SOZqNRTDScmSXQx45tPDVA1Zyq1JVJb5bzxWbLbLeb2+br0rFa8MMDE+gFIKWYG6xqaus5Lo5ew29Dk4Ms2/T+zHmrxV2VJXzVaonv4b9p+pV7nip75a8wgCkQIKOVLn2Ad7o14P3XhC7xyU4J7Y20HlLLynyeZdpo5dXt+GjcxaXf8V3cWmCYRh8FxewtqSjulq1n2s0r5pjttZu1xV7qw3Sr2cd+r9UTSt0np6992aMF5+RcasvJ7h8e9dN9Xqvs9+Q41Y+T3B71031ep7PfkXGrHye4Peum+r1PZr8hxqx8nuD3rpvq9V9nychxuxXR7g966b6vU9mycmTxG1X332M+Z6V0sd9v6L7Pk5NNbFqaX8GEpPnlsRq5umscdmKu8/r2Q+6aS3+6UZcV6lxLhVH5ktyOFqNVk1FuK8/4buPHWkbQ1GuyAKQCbCkQZUU3N5cxmwRM27Ev3KtxKGrxK8p9C4qR7JNH6vWfwx9vR4i0fin7+rzlQiBAAV2fg0wSN9fzxK4jwqVo0qcWtjqc/qXtRp6rLNa8MNvS44tabT8llXd0reOS2ze5fE89rtfGlrtXttLq4sU5J/RFVKk6rznJs8vmzXzW4sk7t+tYrHY1mN9kTYJjaFgmNoUECIpFCCkQAUgEwpECCvVhtPW3Mo+Q3+6N/o3H1mea/p+8MOotw03Vtpjb8V0mxCGWSlV4a80sn7cz9JwTviiXkM8bZZQzMrEQUAIirk0BtY2miVk+WtGVeT5+E21/wAcl6jk6q/+pM8nU01f9OI5ttao6tWU3yvYeD1Gac2Sck/P0+TtUrw12azA+yAGFYhQSQgpBSATIEFACYUiBBSAlcAp5yq1HuSUTvdB4u29/s0dbbuq43wq2DpXtpiEI+JWjqptcko7V2rPuns9HbeJq8/rK9sWcIbjTBFIKWYF3aNeLofhzXJYw904HSVprTLMcrfu6+kjetPs8+Z4Z2gQLMKxACKQUgEFJkAFIBPcFIBMikFA3HR4VQ1FpFSWUpeMz2PRuCcOniJ757Z+7j6jJx5Jlo0jwiGNYRXsptKUlwqcn92a3M6eK/V24mplx8deFR9xQrWtxUt7mm6dalJxnB74s7ETExvDkzWYnaWoAAQVdujn2Nw/0CHuHn+k/h5vK3pLr6Pux/Z5zw7sjMisQAikFIACsSACkABWLZAmFIKAPbhdnK4qqdRfwYvl+8zq9GaGc+TrLR+GP6z/AN72rqc8Ujhjvl0SWR6xyg9zA5fS7RGhjsdfbzVC+islP7s1zS/2Z8OecfZPc182CMnb81X4ngmJ4XVcL2yrU0nkpqPChL81JbDo1y0tG8S0LY71naYR+3mfYfW752LbzPsG5su3R37G2C5rCHuHn+k/hZvK3pLsaSNop9nmPDuxBMKCKQUgNkLetVXCp05Sjzoz4tLmyxxUrMw+LZKVnaZZcTuuomZPYNV/DlOvx8y4lddRMe79V9EnX4+ZcSuuon+w936r6JXr8fMcSuuon+xPd+q+iTr8fMuJXfUTHsGq+iV6/FzLiN3/AG8x7v1X8OTr8XMcRu/7eY9g1X8OT2jF9Rxw+7k/5El52kWvR2rtO3B/yTqcUf7nrtsHefCuZ7OjD/Z09N0L888/aP7tbJrfljTMIRhFRhFJLckd+tK0rFaxtENGZmZ3lkfSAAATSayazQGvi1DqKfcRd5TaBxah1FLuIbybQxuoqNnVUUklTeSS3bDU135bJ/LPoyYvHXzQB4t1YIkqAEFIK99hfUrahwJqTfCz2I7PR/SGLT4eC8Tu1M+C17bw9PytQ6M+w3vfWn5Sw+yXL5XodGfYPfWn5SeyXHyvQ6M+we+tPyk9jyD5Yt+jPsHvrT8pPY8jKlilGrUjTjGecnks0ZMXS2HJeKVid5S2lvWJmUgdRrAAAAAAAAAAAAADTefVK3+OXsNXXflcn8s+jJi8cebnjxbqQCKQUgpAJkCCk2gE3sBEkRW+w+u0f1o29D+Zp5seb4dnUHtnGAAAAAAAAAAAAAGm8+qVv8cvYauu/LZPKfR94vHHm508U60AKQUgEyACkB7cJtY3FVzqLOMOTnZ1uitHTUXm9+2IauqyzSNoTcqMHHgOMeDzZbD004qTXh2jZzuKd99+1z+KW0bW54NP6Elwl+W08l0npa6fNtXumN/8Orp8s5Kdve1WD/8AtofrRh0P5qnm+83w7OpPbuMAAAAAAAAAAAAANdeKlQqRe5xaMWesWxWrPziX1WdrRLmszwrrwApBSIEFAGLYVJ4DN62rHkyTO70HeeO9fk0tbEbRKYcnnkeinu3aCCxyTleRT3KCy7WeV6ZvM6iI5R+8uno4jq5n9XlsPrtD/IjT0P5mnnDNm+HZ1R7dxQAAAAAAf//Z" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
