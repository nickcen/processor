from pipeline import Pipeline
import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
  filepath = os.path.join(os.path.dirname(__file__), 'pipeline.yml')

  p = Pipeline()
  p.load_pipeline(filepath)
  p.run()