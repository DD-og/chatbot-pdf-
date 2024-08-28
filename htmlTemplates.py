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
        <img src="/Users/devmehta/Desktop/dev/yarrrr.jpeg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
