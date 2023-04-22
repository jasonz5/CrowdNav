import torch
import torch.nn as nn
import torch.nn.utils.rnn as rnn_utils
import logging
from crowd_nav.policy.helpers import mlp
from crowd_nav.policy.multi_human_rl import MultiHumanRL

class ValueEstimatorAttn(nn.Module):
    def __init__(self, config, graph_model):
        super().__init__()
        self.graph_model = graph_model
        #[x]: value_network: the input dim
        self.pooling_network = mlp(config.gcn.X_dim, config.gcn_attn_rl.pooling_dims)
        self.value_network = mlp(config.gcn.X_dim * 2, config.gcn_attn_rl.value_network_dims)

        self.attention_weights = None

    def forward(self, state):
        """ Embed state into a latent space. Take the first row of the feature matrix as state representation.
        """
        assert len(state[0].shape) == 3
        assert len(state[1].shape) == 3

        # only use the feature of robot node as state representation
        # state_embedding = self.graph_model(state)[:, 0, :]
        # value = self.value_network(state_embedding)

        state_embedding = self.graph_model(state)
        robot_state_embedding = state_embedding[:, 0, :]
        humans_state_embedding = state_embedding[:, 1:, :]
        # A = self.graph_model(state).get_A()
        human_state_embedding_sum = torch.mean(humans_state_embedding, dim=1)
        weighted_human_feature = self.pooling_network(human_state_embedding_sum)

        # concatenate robot's state with weighted humans' state
        joint_state = torch.cat([robot_state_embedding, weighted_human_feature], dim=1)
        value = self.value_network(joint_state)

        return value
