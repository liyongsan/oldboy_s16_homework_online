import pika
import uuid,time


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='10.143.117.28'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, #只要收到消息就执行on_response
                                   no_ack=True,     #不用ack确认
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:    #验证码核对
            self.response = body


    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        print(self.corr_id)
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,    #发送返回信息的队列name
                                       correlation_id=self.corr_id,     #发送uuid 相当于验证码
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()   #非阻塞版的start_consuming
            print("no messages")
            time.sleep(0.5)     #测试
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()    #实例化
print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)       #执行call方法
print(" [.] Got %r" % response)