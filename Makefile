export PYTHONPATH=${CURDIR}

all:
	echo Nothing to be done

clean:
	rm -rf .cache MANIFEST dist */__pycache__ *~ */*~ */*.pyc build turtle_pil.egg-info
