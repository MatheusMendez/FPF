FROM selenium/standalone-chrome:104.0


ENV APP_PATH /app

WORKDIR $APP_PATH

COPY . $APP_PATH

RUN sudo mkdir -p $APP_PATH \
  && sudo apt-get update && sudo apt-get install -y \
  python3 \
  python3-pip \
  && sudo apt-get autoremove -y

RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt