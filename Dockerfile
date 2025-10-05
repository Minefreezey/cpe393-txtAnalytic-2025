FROM quay.io/jupyter/base-notebook:python-3.11

# Set working directory
WORKDIR /home/jovyan

#copy and install Python Dependencies

COPY --chown=jovyan:users requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
	fix-permissions /home/jovyan 

