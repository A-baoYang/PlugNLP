FROM python:3.8.12

# install gcloud
RUN apt-get update -y && \ 
    useradd -m ripple && \
    curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz && \
    mkdir -p /usr/local/gcloud && \
    tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz && \
    /usr/local/gcloud/google-cloud-sdk/install.sh

ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

WORKDIR /home/ripple

COPY . /home/ripple/ripple-finer

# install kgbuilder
RUN pip install -i http://nexus.dst.cathayholdings.internal.com.tw/repository/dst-pypi/simple --trusted-host=nexus.dst.cathayholdings.internal.com.tw --no-cache-dir kgbuilder
RUN pip install -e /home/ripple/ripple-finer && \
    chown -R ripple:ripple /home/ripple/ripple-finer

# download model
RUN gsutil -m cp -r gs://dst-financial-knowledge-graph/kgbuilder_models/FiNER .

CMD ["RippleFiNER-inference", "--use_ray", "False", "--device_ids", "-1", "--input_text_list", "歷史上發生過幾次黑天鵝事件，像這次 Covid-19 影響全球經濟，造成大範圍的產業鏈停工"]

